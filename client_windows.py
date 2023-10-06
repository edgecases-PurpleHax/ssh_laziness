import netifaces as ni
import winreg as wr
import socket
import requests

host = socket.gethostname()
ip = ni.ifaddresses(ni.interfaces()[0])[2][0]['addr']
print(host,ip)

r = requests.get(f"http://127.0.0.1?host={host}&ip={ip}") # change to webserver address/domain
