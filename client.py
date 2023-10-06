import requests
import socket
import netifaces as ni

host = socket.gethostname()

ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr'] #change tun0 to the needed interface


r = requests.get(f"http://127.0.0.1?host={host}&ip={ip}")