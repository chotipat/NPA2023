from netmiko import ConnectHandler


def test(dip, result):
    result = result.strip().split("\n")
    success = False
    for line in result:
        line = line.split()
        if (
            len(line) >= 2
            and dip == "172.31.129.3"
            and line[0] == "O"
            and line[1] == "192.168.3.0/24"
        ):
            print("test routing R1 passes")
            success = True
        if (
            len(line) >= 2
            and dip == "172.31.129.4"
            and line[0] == "O"
            and line[1] == "192.168.1.0/24"
        ):
            print("test routing R2 passes")
            success = True
    return success


device_ip = ["172.31.129.3", "172.31.129.4"]
username = "admin"
password = "cisco"

for dip in device_ip:
    device_params = {
        "device_type": "cisco_ios",
        "ip": dip,
        "username": username,
        "password": password,
    }

    with ConnectHandler(**device_params) as ssh:
        config_file = dip + "-exercise-ospf.config"
        result = ssh.send_config_from_file(config_file=config_file)
        result = ssh.send_command("sh ip route vrf control-data")
        success = test(dip, result)
        if success:
            result = ssh.save_config()
