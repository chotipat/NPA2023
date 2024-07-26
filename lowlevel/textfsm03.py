import sys
import re
from netmiko import ConnectHandler
from pprint import pprint

device_ip = "172.31.129.4"
username = "admin"
password = "cisco"

device_params = {
    "device_type": "cisco_ios",
    "ip": device_ip,
    "username": username,
    "password": password,
}

if len(sys.argv) == 3:
    print(f'Do you mean interface "{sys.argv[1]} {sys.argv[2]}"')
    exit()
intf_selected = sys.argv[1]
match = re.search("([a-z]+)\s*(\d/\d|\d)", intf_selected, re.IGNORECASE)
if match:
    intf_selected_name = match.group(1)
else:
    print("Wrong interface name!")
    sys.exit(1)
if match:
    intf_selected_num = match.group(2)
else:
    print("Wrong inteface number!")
    sys.exti(1)

found = False
with ConnectHandler(**device_params) as ssh:
    result = ssh.send_command("sh ip interface brief", use_textfsm=True)
    for intf in result:
        intf_name = intf["interface"]
        if re.search(
            rf"{re.escape(intf_selected_name)}", intf_name, re.IGNORECASE
        ) and re.search(rf"{re.escape(intf_selected_num)}", intf_name, re.IGNORECASE):
            print(f"Interface: {intf_name}")
            print(f"\tIP address = {intf['ip_address']}")
            print(f"\tStatus = {intf['status']}")
            found = True
    if not found:
        print("No interface found")
