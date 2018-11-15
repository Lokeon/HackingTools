#! /usr/bin/env python

import subprocess


subprocess.call(["ifconfig"])

interface = raw_input("interface > ")
new_mac = raw_input("new MAC > ")

# Put [ ] for security
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac ])
subprocess.call(["ifconfig", interface, "up"])

print("Changed")
 
