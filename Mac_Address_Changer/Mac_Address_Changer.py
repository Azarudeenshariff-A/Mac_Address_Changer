#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="To Change The Interface")
parser.add_option("-m", "--mac", dest="mac_add", help="The new mac address")

(values, arguments)=parser.parse_args()

interface = values.interface
mac_add = values.mac_add

print("[+] The new mac_addres changed For "+ interface +" to "+mac_add)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac_add])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig", interface])