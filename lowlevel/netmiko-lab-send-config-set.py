from netmiko import ConnectHandler

device_ip = "172.31.129.3"
username = "admin"
password = "cisco"

device_params = {
    "device_type": "cisco_ios",
    "ip": device_ip,
    "username": username,
    "password": password,
}

commands = [
    "int lo1",
    "ip add 1.1.1.1 255.255.255.255",
    "no shut",
    "int lo2",
    "ip add 2.2.2.2 255.255.255.255",
    "no shut",
]

with ConnectHandler(**device_params) as ssh:
    result = ssh.send_config_set(commands)
    print(result)
    result = ssh.send_command("sh ip int bri")
    print(result)
    result = ssh.save_config()
    print(result)
