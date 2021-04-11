#This program refers to a txt file containing the ip addresses
#of cisco routers and deploys configuration to those routers using netmiko


from netmiko import ConnectHandler


with open('devices.txt') as f:
   devices = f.read().splitlines()

device_list = list()


for ip in devices:
   cisco_device = {
           'device_type': 'cisco_ios',
           'host': ip,
           'username': 'santhosh',
           'password': 'cisco',
           'port': 22,
           'secret': 'cisco', #enable password
           'verbose': True
           }
   device_list.append(cisco_device)



for device in device_list:
    connection = ConnectHandler(**device)

    print('Entering the enable mode ...')
    connection.enable()

    # prompting the user for a config file
    file = input(f'Enter a configuration file (use a valid path) for {device["host"]}:')

    print(f'Running commands from file: {file} on device: {device["host"]}')
    output = connection.send_config_from_file(file)
    print(output)

    print(f'Closing connection to {cisco_device["host"]}')
    connection.disconnect()

    

