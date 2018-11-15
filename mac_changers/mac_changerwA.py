#! /usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface , use -- help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac , use -- help for more info.")
    return options

def change_mac(interface,new_mac):
    # Put [ ] for security
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac ])
    subprocess.call(["ifconfig", interface, "up"])

ops = get_arguments()
change_mac(ops.interface,ops.new_mac)
print("Changed")
 
