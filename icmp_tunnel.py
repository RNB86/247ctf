# this file requires error_reporting.pcap in the same folder as the .py file

from scapy.all import *

from scapy.layers.inet import ICMP

fname = "error_reporting.pcap"

network_packets = rdpcap(fname)
pdata = bytes()

p_number = 0
while (p_number < 1712):
    p = network_packets[p_number]
    if p_number > 0:
        pdata += p[ICMP].payload.fields['load']
    p_number += 1

print(pdata)

with open("my_raw.jpg","wb") as binary_file:
    binary_file.write(pdata)
