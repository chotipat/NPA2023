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
match = re.search("([A-Za-z]+)\s*(\d/\d|\d)", intf_selected, re.IGNORECASE)
if match:
    intf_selected_name = match.group(1)
    intf_selected_num = match.group(2)
else:
    print("Wrong interface name format!")
    sys.exit(1)

found = False
with ConnectHandler(**device_params) as ssh:
    result = ssh.send_command("sh ip interface brief", use_textfsm=True)
    intf_selected_name = "^" + intf_selected_name
    intf_selected_num = "^" + intf_selected_num
    for intf in result:
        intf_name = intf["interface"]
        intf_name_alpha = re.search("([A-Za-z]*)(\d.*)", intf_name).group(1)
        intf_name_num = re.search("([A-Za-z]*)(\d.*)", intf_name).group(2)
        if re.search(intf_selected_name, intf_name_alpha, re.IGNORECASE) and re.search(
            intf_selected_num, intf_name_num, re.IGNORECASE
        ):
            print(f"Interface: {intf_name}")
            print(f"\tIP address = {intf['ip_address']}")
            print(f"\tStatus = {intf['status']}")
            found = True
    if not found:
        print("No interface found")
