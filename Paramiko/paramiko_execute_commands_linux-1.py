'''
This is a program to establish a SSh connection with a remote linux machine.
This uses invoke_shell() to request and interactive shell session and execute the commands.
''' 


import paramiko
import time
import getpass

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

password=getpass.getpass(prompt="Etner your password: ")
linux = {'hostname': '10.0.0.1', 'port': '22', 'username':'santhosh', 'password': password}
print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('cat /etc/passwd\n')
time.sleep(1)

shell.send('sudo cat /etc/shadow\n')
shell.send('pass123\n')
time.sleep(1)


output = shell.recv(10000)
output = output.decode('utf-8')
print(output)


if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()