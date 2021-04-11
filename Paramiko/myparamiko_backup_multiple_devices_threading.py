'''
This is a program to backup the running configuration of multiple cisco routers.
The backups of multiple routers are done parallely by using multithreading which is implemented by using the threading module.
'''


import myparamiko # myparamiko.py should be in the same directory with this script (or in sys.path)
import threading


def backup(router):
    client = myparamiko.connect(**router)
    shell = myparamiko.get_shell(client)

    myparamiko.send_command(shell, 'terminal length 0')
    myparamiko.send_command(shell, 'enable')
    myparamiko.send_command(shell, 'cisco') 
    myparamiko.send_command(shell, 'show run')

    output = myparamiko.show(shell)

    output_list = output.splitlines()
    output_list = output_list[11:-1]
    output = '\n'.join(output_list)

    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    file_name = f'{router["server_ip"]}_{year}-{month}-{day}.txt'
    with open(file_name, 'w') as f:
        f.write(output)

    myparamiko.close(client)

router1 = {'server_ip':'10.0.0.1', 'server_port': '22', 'user': 'santhosh', 'passwd': 'cisco'}
router2 = {'server_ip':'10.0.0.2', 'server_port': '22', 'user': 'santhosh', 'passwd': 'cisco'}
router3 = {'server_ip':'10.0.0.3', 'server_port': '22', 'user': 'santhosh', 'passwd': 'cisco'}


routers = [router1, router2, router3]

# creating an empty list ,it will store the threads
threads = list()
for router in routers:
    # creating a thread for each router that executes the backup function
    th = threading.Thread(target=backup, args=(router,))
    threads.append(th) 

# starting the threads
for th in threads:
    th.start()

# waiting for the threads to finish
for th in threads:
    th.join()