#!/usr/bin/python3 python3

import subprocess
import optparse

def parse_input():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="The interface name.")
    parser.add_option("-m", "--new_mac", dest="new_mac", help="The new MAC.")
    (opts, args) = parser.parse_args()
    if not opts.interface:
        parser.error("[-] You have to enter the interface name => (Check `python3 mac-changer.py -h` for more info).")
    elif not opts.new_mac:
        parser.error("[-] You have to enter the new MAC address => (Check `python3 mac-changer.py -h` for more info).")
    return opts 

def change_mac(interface, new_mac):
    print("[+] Changing the address for interface " + interface + " to MAC address of " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = parse_input()

change_mac(options.interface, options.new_mac)
