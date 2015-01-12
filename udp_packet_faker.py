#!/usr/bin/env python
import sys
from scapy.all import *

if len(sys.argv) != 5:
    print "Usage: ./udp_packet_faker.py <target> <spoofed_ip> <port> <payload>"
    sys.exit(1)

target = sys.argv[1]
spoofed_ip = sys.argv[2]
port = int(sys.argv[3])
payload = sys.argv[4]


packet = IP(dst=target,src=spoofed_ip) / UDP(dport=port,sport=5000) / ("B00Bs:"+payload)
send(packet)
print "Packet sent!"
