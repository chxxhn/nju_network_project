'''
Ethernet learning switch with Least Traffic Volume (LTV) mechanism in Python.

This file has been updated to implement a learning switch with a Least Traffic Volume (LTV) mechanism.
'''
from switchyard.lib.userlib import *

def main(net):
    my_interfaces = net.interfaces()
    mymacs = [intf.ethaddr for intf in my_interfaces]
    
    # MAC address table with traffic volume and max entries
    mac_table = {}
    max_entries = 2  # Maximum number of entries in the table

    while True:
        try:
            timestamp, input_port, packet = net.recv_packet()
        except NoPackets:
            continue
        except Shutdown:
            return

        log_info("In {} received packet {} on {}".format(net.name, packet, input_port))

        src_mac = packet[0].src
        dst_mac = packet[0].dst

        # Step 1: Add or update the source MAC address in the table without increasing traffic volume
        if src_mac not in mac_table:
            # Check if the table is full
            if len(mac_table) >= max_entries:
                # Remove entry with the lowest traffic volume
                lowest_traffic_mac = min(mac_table, key=lambda k: mac_table[k][1])
                log_info("Table full. Removing entry with lowest traffic volume: MAC {} from port {}".format(lowest_traffic_mac, mac_table[lowest_traffic_mac][0]))
                del mac_table[lowest_traffic_mac]
            # Add the new entry with traffic_volume set to 0
            log_info("Learning MAC {} on port {}".format(src_mac, input_port))
            mac_table[src_mac] = (input_port, 0)
        else:
            # Update the port if the MAC is known, without modifying traffic volume
            if mac_table[src_mac][0] != input_port:
                log_info("Updating MAC {} to new port {} without modifying traffic volume".format(src_mac, input_port))
                mac_table[src_mac] = (input_port, mac_table[src_mac][1])

        # Step 2: Check if the packet is intended for the switch itself
        if dst_mac in mymacs:
            log_info("Packet intended for me")
            continue

        # Step 3: Forward the packet based on the destination MAC address
        if dst_mac in mac_table:
            # Known destination MAC address
            output_port, traffic_volume = mac_table[dst_mac]
            if output_port != input_port:
                log_info("Sending packet {} to {}".format(packet, output_port))
                net.send_packet(output_port, packet)
                # Increment traffic volume on HIT
                mac_table[dst_mac] = (output_port, traffic_volume + 1)
            else:
                log_info("Destination is on the same port as source. Dropping packet.")
        else:
            # Unknown destination MAC address - flood to all ports except the input port
            log_info("Unknown destination MAC. Flooding packet {} to all ports except {}".format(packet, input_port))
            for intf in my_interfaces:
                if intf.name != input_port:
                    net.send_packet(intf.name, packet)

    net.shutdown()
