#!/usr/bin/python3 python3

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="int", help="The interface name.")
parser.add_option("-m", "--new_mac", dest="mac", help="The new MAC.")
(opts, args) = parser.parse_args()

subprocess.call(["ifconfig", opts.int, "down"])
subprocess.call(["ifconfig", opts.int, "hw", "ether", opts.mac])
subprocess.call(["ifconfig", opts.int, "up"])

print("[+] The address for interface " + opts.int + " changed successfully to MAC address of " + opts.mac)
