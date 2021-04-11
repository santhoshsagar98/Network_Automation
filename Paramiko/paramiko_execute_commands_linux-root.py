'''
This is program that uses paramiko module to connect to a linux machine through SSH.
Then it uses the exec_comman() function to execute the models. 
The output from these commands are written back into three variables as python file like objects which can be used to read the ouput, read the error or write in the shell.
'''

import paramiko
import time
import getpass

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

password= getpass.getpass(prompt="Enter your password: ")
linux = {'hostname': '10.0.0.1', 'port': '22', 'username':'santhosh', 'password': password}
print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('sudo useradd u2\n', get_pty=True)

stdin.write('password123\n')  # this is the sudo password
time.sleep(2)  #waiting for the remote server to finish

stdin, stdout, stderr = ssh_client.exec_command('cat /etc/passwd\n')
print(stdout.read().decode())
time.sleep(1)


if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()