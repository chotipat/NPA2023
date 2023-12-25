import time
import paramiko

USERNAME = "admin"
PASSWORD = "cisco"

devices_ip = ["172.31.129.4"]

for ip in devices_ip:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=ip, username=USERNAME, password=PASSWORD, look_for_keys=False
    )

    # commands = ["sh ip int br", "sh interfaces"]
    commands = ["sh ip int br"]
    for command in commands:
        print("Executing {}".format(command))
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode())
        print("Errors")
        print(stderr.read().decode())
        time.sleep(1)
    client.close()
