#!/usr/bin/python3 python3

import subprocess
import optparse
import re

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
    print("[+] Changing the MAC address for interface " + interface + " to MAC address of " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_interface_mac(interface):
    ifconfig_interface_result = subprocess.check_output(["ifconfig", interface])
    # \w\w:\w\w:\w\w:\w\w:\w\w:\w\w
    search_match = re.search(r"(\w\w:){5}(\w\w){1}", str(ifconfig_interface_result))
    if not search_match:
        return None 
    else:
        return search_match.group(0)



options = parse_input()

current_mac = get_interface_mac(options.interface)
if not current_mac:
    print("[-] This interface does not have a MAC address")
elif current_mac == options.new_mac:
    print("[-] This MAC is already assigned to this interface.")    
else:
    print("[+] The current MAC address is: " + current_mac)
    change_mac(options.interface, options.new_mac)
    current_mac = get_interface_mac(options.interface)
    if current_mac == options.new_mac:
        print("[+] The MAC address for the interface " + options.interface + " changed sucessfully to " + options.new_mac)
    else:
        print("[-] The MAC changing faild => try to run the script as an administrator using `sudo` prefix before running python commang")
