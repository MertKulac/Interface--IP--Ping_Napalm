from napalm import get_network_driver
from ping3 import ping
from ipaddress import ip_network, ip_address
import pprint

driver = get_network_driver('huawei_vrp')
device = driver(hostname='X.X.X.X', username='admin', password='admin')
device.open()

#  Return general device information
get_interfaces_ip = device.get_interfaces_ip()
print(get_interfaces_ip)

for i in get_interfaces_ip:
        if "Virtual-Ether" in i:
                interface = get_interfaces_ip[i]["ipv4"]
                ip_list = list(interface.keys())
                print(ip_list)

                for j in ip_list:
                        ping_remote_ip = device.ping(j)
                        pprint.pprint(ping_remote_ip)
                    
