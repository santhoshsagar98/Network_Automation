'''
This program helps troubleshooting netmiko by obtaining the logging file
from the router and displaying it. 
http://ktbyers.github.io/netmiko/COMMON_ISSUES.html
'''

from netmiko import ConnectHandler
import time
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")


cisco_device = {
       'device_type': 'cisco_ios',
       'host': '10.1.1.10',
       'username': 'u1',
       'password': 'cisco',
       'port': 22,             # optional, default 22
       'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }
connection = ConnectHandler(**cisco_device)
output = connection.send_command('show version')
print(output)

connection.write_channel('show version\n')
time.sleep(2)
output = connection.read_channel()
print(output)
print('Closing connection')
connection.disconnect()