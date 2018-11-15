#! /usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i","--interface", dest="interface", help="Interface to change MAC address")
parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")

(options, arguments) = parser.parse_args()

# Put [ ] for security
subprocess.call(["ifconfig", options.interface, "down"])
subprocess.call(["ifconfig", options.interface, "hw", "ether", options.new_mac ])
subprocess.call(["ifconfig", options.interface, "up"])

print("Changed")
 
