# This program is for reading ospf configuration from a text file and deploying to a cisco router


from netmiko import ConnectHandler
cisco_device = {
       'device_type': 'cisco_ios',
       'host': '10.0.0.1',
       'username': 'santhosh',
       'password': 'cisco',
       'port': 22,             
       'secret': 'cisco',      # enable password
       'verbose': True        
       }
connection = ConnectHandler(**cisco_device)
print('Entering the enable mode...')
connection.enable()

print('Sending commands from file ...')
output = connection.send_config_from_file('ospf.txt')
print(output)

print('Closing connection')
connection.disconnect()