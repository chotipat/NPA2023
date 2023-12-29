from netmiko import ConnectHandler
import time


def test(dip, interface, result):
    success = False
    if "!!!!" in result:
        print(
            "Pass: Ping from", dip, "interface", interface, "to 8.8.8.8 is successful."
        )
        success = True
    else:
        print("Fail: Ping from", dip, "interface", interface, "to 8.8.8.8 is failed.")
    return success


device_ip = ["172.31.129.4", "172.31.129.3"]
username = "admin"
password = "cisco"

success_count = 0
for dip in device_ip:
    device_params = {
        "device_type": "cisco_ios",
        "ip": dip,
        "username": username,
        "password": password,
    }

    success = True
    with ConnectHandler(**device_params) as ssh:
        if dip == "172.31.129.4":
            config_file = "config/" + dip + "-exercise-nat.txt"
            ssh.send_config_from_file(config_file=config_file)
        for interface in ["g0/1", "g0/2"]:
            result = ssh.send_command(
                "ping vrf control-data 8.8.8.8 source " + interface
            )
            success = success and test(dip, interface, result)
            if success:
                success_count += 1
        if success:
            result = ssh.save_config()

print("Pass", success_count, "tests of total 4 tests.")
