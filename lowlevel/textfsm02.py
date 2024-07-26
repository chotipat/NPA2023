from netmiko import ConnectHandler
from pprint import pprint

device_ip = '172.31.112.4'
username = 'admin'
password = 'cisco'

device_params = {'device_type': 'cisco_ios',
                 'ip': device_ip,
                 'username': username,
                 'password': password,
                }

with ConnectHandler(**device_params) as ssh:
    result = ssh.send_command('sh ip interface brief', use_textfsm=True)
    pprint(result)



