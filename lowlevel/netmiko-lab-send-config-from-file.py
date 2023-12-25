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

with ConnectHandler(**device_params) as ssh:
    config_file = device_ip + "-lab.config"
    result = ssh.send_config_from_file(config_file=config_file)
    print(result)
    result = ssh.send_command("sh ip int bri")
    print(result)
    result = ssh.save_config()
    print(result)
