#! /usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface , use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac , use --help for more info.")
    return options

def change_mac(interface,new_mac):
    # Put [ ] for security
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac ])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconf_res = subprocess.check_output(["ifconfig", interface])
    # rule to found MAC on ifconfig
    mac_address_res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconf_res)
    if mac_address_res:
        return mac_address_res.group(0)
    else:
        print("[-] Could not read MAC address.")

def compr_mac(current_mac,new_mac):
    if current_mac == new_mac:
        #casting for none result 
        print("[+] MAC Address changed to "+ str(current_mac))
    else:
        print("[-] MAC address didn't get changed")

ops = get_arguments()
current_mac = get_current_mac(ops.interface)
#casting for none result 
print("Current MAC = "+ str(current_mac))

change_mac(ops.interface,ops.new_mac)
print("[+] Changing ")

current_mac = get_current_mac(ops.interface)
compr_mac(current_mac,ops.new_mac)