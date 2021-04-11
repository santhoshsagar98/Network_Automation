'''
This is program to connect to mutiple cisco routers using SSH. This is done by using myparamiko module which is a separate program written and uploaded before.
This program obtains the information of the devices and backs up the running configuration with the time, date and year.
'''


import myparamiko # myparamiko.py should be in the same directory with this script (or in sys.path)
import time
import getpass

password1=getpass.getpass(prompt="Etner your password for router 1: ")
password2=getpass.getpass(prompt="Etner your password for router 2: ")
password3=getpass.getpass(prompt="Etner your password for router 3: ")
router1 = {'server_ip':'10.1.1.10', 'server_port': '22', 'user': 'u1', 'passwd': password1}
router2 = {'server_ip':'10.1.1.20', 'server_port': '22', 'user': 'u1', 'passwd': password2}
router3 = {'server_ip':'10.1.1.30', 'server_port': '22', 'user': 'u1', 'passwd': password3}


routers = [router1, router2, router3]


for router in routers:
    client = myparamiko.connect(**router)
    shell = myparamiko.get_shell(client)

    myparamiko.send_command(shell, 'terminal length 0')
    myparamiko.send_command(shell, 'enable')
    myparamiko.send_command(shell, 'cisco')  # this is the enable command
    myparamiko.send_command(shell, 'show run')

    output = myparamiko.show(shell)

    # processing the output
    output_list = output.splitlines()
    output_list = output_list[11:-1]
    output = '\n'.join(output_list)

    # creating the backup filename
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    file_name = f'{router["server_ip"]}_{year}-{month}-{day}.txt'
    print(file_name)

    # writing the backup to the file
    with open(file_name, 'w') as f:
        f.write(output)

    myparamiko.close(client)
