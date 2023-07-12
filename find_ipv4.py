

import psutil

interfaces = psutil.net_if_addrs()
# interfaces['wlp1s0'] #Linux
# interfaces['Wi-Fi'] #Windows

    
def get_wlan_ipv4_address():
    interfaces = psutil.net_if_addrs()
    for interface_name, interface_addresses in interfaces.items():
        if "Wi-Fi" in interface_name or 'wlp1s0' in interface_name:
            for address in interface_addresses:
                if address.family.name == "AF_INET":
                    ipv4_address = address.address
                    return ipv4_address
    return None

wlan_ipv4_address = get_wlan_ipv4_address()
if wlan_ipv4_address:
    print(f"WLAN IPv4 Address: {wlan_ipv4_address}")
    with open("ip_address.txt", 'w') as f:
        f.write(wlan_ipv4_address)
else:
    print("WLAN interface not found or does not have an IPv4 address.")

