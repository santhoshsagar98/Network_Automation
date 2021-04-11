'''
This program is for connecting to the cisco router visa ssh and checking if its in global config mode. If not it will call the config_mode() function to move to global config mode
'''

from netmiko import ConnectHandler
cisco_device = {
       'device_type': 'cisco_ios', 
       'host': '10.0.0.1',
       'username': 'santhosh',
       'password': 'cisco',
       'port': 22,            
       'secret': 'cisco',  # enable password    
       'verbose': True        
       }
connection = ConnectHandler(**cisco_device)

# getting the router's prompt
prompt = connection.find_prompt()
if '>' in prompt:
       connection.enable()   # entering the enable mode

output = connection.send_command('sh run')
print(output)

if not connection.check_config_mode(): 
       connection.config_mode()  # entering the global config mode

# print(connection.check_config_mode())
connection.send_command('username u3 secret cisco')

connection.exit_config_mode()  # exiting the global config mode
print(connection.check_config_mode())

print('Closing connection')
connection.disconnect()