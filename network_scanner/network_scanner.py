#! /usr/bin/env python

from scapy.all import *

def scan(ip):
    arp_request = scapy.all.ARP(pdst=ip)
    #arp_request.pdst = ip
    print(arp_request.summary())
    
scan("10.20.14.1/24")