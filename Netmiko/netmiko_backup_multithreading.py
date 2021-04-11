'''
 This program reads the ip address of routers from a txt file and backs up the
running configuration parallely by using multi-threading
'''

from netmiko import ConnectHandler
from datetime import datetime
import time
import threading  #implements threading 


start = time.time()


# target function which gets executed by each thread
def backup(device):
    connection = ConnectHandler(**device)
    print('Entering the enable mode...')
    connection.enable()

    output = connection.send_command('show run')
    prompt = connection.find_prompt()
    hostname = prompt[0:-1]

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    filename = f'{hostname}_{year}-{month}-{day}_backup.txt'
    with open(filename, 'w') as backup:
        backup.write(output)
        print(f'Backup of {hostname} completed successfully')
        print('#' * 30)

    print('Closing connection')
    connection.disconnect()



with open('devices.txt') as f:
    devices = f.read().splitlines()

# creating an empty list to store the threads
threads = list()
for ip in devices:
    device = {
           'device_type': 'cisco_ios',
           'host': ip,
           'username': 'santhosh',
           'password': 'cisco',
           'port': 22,             
           'secret': 'cisco',      # enable password
           'verbose': True       
           }
    # creating a thread for each router that executes the backup function
    th = threading.Thread(target=backup, args=(device,))
    threads.append(th) 

# starting the threads
for th in threads:
    th.start()

# waiting for the threads to finish
for th in threads:
    th.join()

end = time.time()
print(f'Total execution time:{end-start}')
