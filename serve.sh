#!/bin/bash 
python3 /home/andreasergi/Documents/http_wlan/find_ipv4.py
value=$(</home/andreasergi/Documents/http_wlan/ip_address.txt)  
echo "$value"  
python3 -m http.server -b $value