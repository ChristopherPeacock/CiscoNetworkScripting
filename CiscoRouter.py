from netmiko import ConnectHandler
from config import CSR 


net_connect = ConnectHandler(**CSR)
output = net_connect.send_command('show ip interface brief')
print(output)

net_connect.disconnect()