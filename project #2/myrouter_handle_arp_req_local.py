from switchyard.lib.userlib import *

class Router(object):
    def __init__(self, net):
        self.net = net
        self.interfaces = net.interfaces()
        self.ip_to_mac = {str(list(intf.ipaddrs)[0].ip): intf.ethaddr for intf in self.interfaces if intf.ipaddrs}

    def router_main(self):
        while True:
            try:
                timestamp, dev, packet = self.net.recv_packet(timeout=1.0)
            except NoPackets:
                continue
            except Shutdown:
                break

            arp = packet.get_header(Arp)
            if arp is None or arp.operation != ArpOperation.Request:
                continue

            target_ip = str(arp.targetprotoaddr)
            if target_ip in self.ip_to_mac:
                mac_addr_found = self.ip_to_mac[target_ip]
            else:
                continue

            arp_reply = create_ip_arp_reply(
                srchw=mac_addr_found,
                dsthw=arp.senderhwaddr,
                srcip=arp.targetprotoaddr,
                targetip=arp.senderprotoaddr
            )

            self.net.send_packet(dev, arp_reply)
            log_info(f"Sent ARP Reply on {dev}: {arp_reply}")

def main(net):
    r = Router(net)
    r.router_main()
    net.shutdown()
