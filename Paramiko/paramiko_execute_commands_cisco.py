'''
This is a program to establish a SSH connection with a cisco router using the paramiko module and execute commands.
invoke_shell() is used to request an interactive shell session and a shell object is creared to send the commands.
'''



import paramiko
import time
import getpass


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

password=getpass.getpass(prompt="Etner your password: ")
router = {'hostname': '10.0.0.1', 'port': '22', 'username':'santhosh', 'password':password}
print(f'Connecting to {router["hostname"]}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

# creating a shell object
shell = ssh_client.invoke_shell()


shell.send('terminal length 0\n')
shell.send('show version\n')
shell.send('show ip int brief\n')
time.sleep(1)  # waiting for the remove device to finish executing the commands (mandatory)

# reading from the shell's output buffer
output = shell.recv(10000)
output = output.decode('utf-8')  # decoding from bytes to string
print(output)


if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()