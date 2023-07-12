@echo off


@REM C:\Users\Docplanner\Desktop\python\http_wlan
python C:\Users\Docplanner\Desktop\python\http_wlan\get_ipv4.py && shutdown /r /f /t 86400
for /f "delims=" %%x in (ip_address.txt) do set addr=%%x
python -m http.server -b %addr%