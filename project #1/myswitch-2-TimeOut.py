'''
Ethernet learning switch with TimeOut in Python.

This file has been updated to implement a learning switch with a timeout mechanism.
'''
from switchyard.lib.userlib import *
import time

def main(net):
    my_interfaces = net.interfaces()
    mymacs = [intf.ethaddr for intf in my_interfaces]
    
    # MAC address table with timestamp
    mac_table = {}
    timeout = 10  # Timeout set to 10 seconds

    while True:
        try:
            timestamp, input_port, packet = net.recv_packet()
        except NoPackets:
            continue
        except Shutdown:
            return

        current_time = time.time()
        log_info("In {} received packet {} on {}".format(net.name, packet, input_port))

        # Remove expired entries from mac_table
        for mac, (port, last_seen) in list(mac_table.items()):
            if current_time - last_seen > timeout:
                log_info("Removing expired MAC entry {} from port {}".format(mac, port))
                del mac_table[mac]

        # Step 1: Learn the source MAC address and associate it with the input port
        src_mac = packet[0].src
        if src_mac not in mac_table:
            log_info("Learning MAC {} on port {}".format(src_mac, input_port))
        mac_table[src_mac] = (input_port, current_time)
        else:
            # Update the timestamp if src_mac already exists
            if mac_table[src_mac][0] != input_port:
                log_info("Updating MAC {} to new port {}".format(src_mac, input_port))
            mac_table[src_mac] = (input_port, current_time)

        # Step 2: Check if the packet is intended for the switch itself
        if packet[0].dst in mymacs:
            log_info("Packet intended for me")
            continue

        # Step 3: Forward the packet based on the destination MAC address
        dst_mac = packet[0].dst
        if dst_mac in mac_table:
            # Known destination MAC address
            output_port = mac_table[dst_mac][0]
            if output_port != input_port:
                log_info("Sending packet {} to {}".format(packet, output_port))
                net.send_packet(output_port, packet)
            else:
                log_info("Destination is on the same port as source. Dropping packet.")
        else:
            # Unknown destination MAC address - flood to all ports except the input port
            log_info("Unknown destination MAC. Flooding packet {} to all ports except {}".format(packet, input_port))
            for intf in my_interfaces:
                if intf.name != input_port:
                    net.send_packet(intf.name, packet)

    net.shutdown()
