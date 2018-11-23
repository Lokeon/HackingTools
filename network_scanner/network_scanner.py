#! /usr/bin/env python

import scapy.all as scapy
import argparse

def get_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("-t","--target", dest="target", help="Put IP of Gateway with /MAC")
        options = parser.parse_args()
        if not options.target:
                parser.error("[-] Please specify an ip , use --help for more info.")
        return options

def scan(ip):
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        # / to combine lolz
        arp_request_broadcast = broadcast/arp_request
        # srp return two list, but just need the answered one
        # answered_list (packet_sent , answered)
        answered_list = scapy.srp(
                arp_request_broadcast, timeout=1, verbose=False)[0]

        clients_list = []
        for element in answered_list:
                clients_dic = {"ip": element[1].psrc, "mac": element[1].hwsrc}
                clients_list.append(clients_dic)
        return clients_list


def print_result(result_list):
        print("IP\t\t\tMAC ADRESS\n- - - - - - - - - - - - - - - - - - - - - -")
        for client in result_list:
                print(client["ip"] + "\t\t" + client["mac"])

ops = get_arguments()
scan_result = scan(ops.target)
print_result(scan_result)