#!/usr/bin/env python3

'''
Basic IPv4 router (static routing) in Python.
'''

import sys
import os
import time
from switchyard.lib.userlib import *

class Router(object):
    def __init__(self, net):
        self.net = net
        # Router 인터페이스 정보 저장
        self.interfaces = self.net.interfaces()
        # IP/MAC 매핑 정보를 저장할 룩업 테이블 생성
        self.arp_table = {str(list(intf.ipaddrs)[0].ip): intf.ethaddr for intf in self.interfaces if intf.ipaddrs}

    def router_main(self):    
        '''
        Main method for router; we stay in a loop in this method, receiving
        packets until the end of time.
        '''
        while True:
            gotpkt = True
            try:
                # this router waits for a second to receive packets
                # if no packet arrives in a second, NoPackets except occurs
                timestamp, dev, pkt = self.net.recv_packet(timeout=1.0)
            except NoPackets:
                log_info("No packets available in recv_packet")
                gotpkt = False
            except Shutdown:
                log_info("Got shutdown signal")
                break

            if gotpkt:
                log_info("Got a packet: {}".format(str(pkt)))
                arp = pkt.get_header(Arp)
                if arp is None or arp.operation != ArpOperation.Request:
                    continue  # ARP 패킷이 아니거나 Request가 아닐 경우 무시

                # ARP Request 메시지의 송신자 정보 저장 (IP/MAC 매핑)
                sender_ip = str(arp.senderprotoaddr)
                sender_mac = arp.senderhwaddr
                self.arp_table[sender_ip] = sender_mac

                # ARP Request 메시지가 라우터의 IP 주소나 캐시에 있는 IP 주소를 질의하는지 확인
                target_ip = str(arp.targetprotoaddr)
                if target_ip in self.arp_table:
                    mac_addr_found = self.arp_table[target_ip]
                else:
                    continue  # 응답할 수 없는 경우 무시

                # ARP Reply 생성 및 송신
                arp_reply = create_ip_arp_reply(
                    srchw=mac_addr_found,
                    srcip=arp.targetprotoaddr,
                    dsthw=arp.senderhwaddr,
                    targetip=arp.senderprotoaddr
                )

                log_info(f"Sending ARP Reply: {arp_reply}")
                self.net.send_packet(dev, arp_reply)

def main(net):
    '''
    Main entry point for router.  Just create Router
    object and get it going.
    '''
    r = Router(net)
    r.router_main()
    net.shutdown()
