#! /usr/bin/env python

from scapy.all import *

def scan(ip):
    arp_request = scapy.all.ARP(pdst=ip)
    broadcast = scapy.all.Ether(dst="ff:ff:ff:ff:ff:ff")
    # / to combine lolz
    arp_request_broadcast = broadcast/arp_request
    # srp return two list, but just need the answered one 
    # answered_list (packet_sent , answered)
    answered_list = scapy.all.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
 
    print("IP\t\t\tMAC ADRESS\n- - - - - - - - - - - - - - - - - - - - - -")
    clients_list = []
    for element in answered_list:
        clients_dic = {"ip":element[1].psrc,"mac":element[1].hwsrc}
        clients_list.append(clients_dic)
        print(element[1].psrc + "\t\t" + element[1].hwsrc )  
    
scan("10.20.14.1/24")