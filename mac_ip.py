import getmac # mac_address
import socket # ip_address


print(getmac.get_mac_address())
hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)
print(ip)
