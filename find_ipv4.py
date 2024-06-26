

import psutil
import json

interfaces = psutil.net_if_addrs()
for interface_name, interface_addresses in interfaces.items():
    int_json = {interface_name: interface_addresses}
    print(f"{interface_name}: {interface_addresses}")

# with open('/home/andreasergi/Documents/Repos/http_wlan/interfaces_ubuntu.json', 'w') as f:
#     f.write(json.dumps(int_json))
# interfaces['wlp1s0'] #Linux
# interfaces['Wi-Fi'] #Windows

    
def get_wlan_ipv4_address():
    interfaces = psutil.net_if_addrs()
    ipv4_address_eth = None
    ipv4_address = None
    for interface_name, interface_addresses in interfaces.items():
        if "enx" in interface_name or 'enp2s' in interface_name or 'eth' in interface_name:
            for address in interface_addresses:
                if address.family.name == 'AF_INET':
                    ipv4_address_eth = address.address
        if "Wi-Fi" in interface_name or 'wlp1s0' in interface_name or 'wlan0' in interface_name:
            for address in interface_addresses:
                if address.family.name == "AF_INET":
                    ipv4_address = address.address
                    # return ipv4_address
        if ipv4_address_eth:
            return ipv4_address_eth

    return ipv4_address
    # return None

wlan_ipv4_address = get_wlan_ipv4_address()
if wlan_ipv4_address:
    print(f"WLAN IPv4 Address: {wlan_ipv4_address}")
    # with open("/home/andreasergi/Documents/Repos/http_wlan/ip_address.txt", 'w') as f:
    # with open("/home/andreasergi/Documents/http_wlan/ip_address.txt", 'w') as f:
    with open("/home/andreasergi/Documents/http-server-fs/ip_address.txt", 'w') as f:
        f.write(wlan_ipv4_address)
else:
    print("WLAN interface not found or does not have an IPv4 address.")

