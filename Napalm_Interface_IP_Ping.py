from napalm import get_network_driver
from ping3 import ping
from ipaddress import ip_network, ip_address

driver = get_network_driver('huawei_vrp')
device = driver(hostname='172.28.111.86', username='NPESCRIPT', password='RYXga421')
device.open()


#  Return general device information
get_interfaces_ip = device.get_interfaces_ip()

for i in get_interfaces_ip:
        if "Virtual-Ether" in i:
                interface = get_interfaces_ip[i]["ipv4"]
                ip_list = list(interface.keys())
                #print(ip_list)
                for j in ip_list:
                        send_command = device.cli(['ping {}'.format(j)])
                        print(send_command)
                    
