import paramiko
import time

username = "admin"

devices_ip = ["172.31.129.4"]
mykey = paramiko.RSAKey.from_private_key_file("/Users/chotipat/.ssh/adminR2_id_rsa")

for ip in devices_ip:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=ip,
        username=username,
        disabled_algorithms={"pubkeys": ["rsa-sha2-256", "rsa-sha2-512"]},
        pkey=mykey,
    )

    with client.invoke_shell() as ssh:
        print("Connected to {} ...".format(ip))

        ssh.send("conf t\n")
        time.sleep(1)

        ssh.send("int g0/1\n")
        time.sleep(1)
        ssh.send("vrf forwarding control-data\n")
        time.sleep(1)
        ssh.send("ip address 192.168.2.2 255.255.255.0\n")
        time.sleep(1)
        ssh.send("no shut\n")
        time.sleep(1)
        ssh.send("exit\n")

        ssh.send("int g0/2\n")
        time.sleep(1)
        ssh.send("vrf forwarding control-data\n")
        time.sleep(1)
        ssh.send("ip address 192.168.3.1 255.255.255.0\n")
        time.sleep(1)
        ssh.send("no shut\n")
        time.sleep(1)
        ssh.send("exit\n")

        ssh.send("int g0/3\n")
        time.sleep(1)
        ssh.send("vrf forwarding control-data\n")
        time.sleep(1)
        ssh.send("ip address dhcp\n")
        time.sleep(1)
        ssh.send("no shut\n")
        time.sleep(1)
        ssh.send("end\n")
        # wait longer to get IP from DHCP
        time.sleep(20)

        ssh.send("sh ip vrf interface control-data\n")
        time.sleep(2)
        output = ssh.recv(5000).decode("ascii")
        output = output.split()
        expected_ip = {
            "Gi0/1": "192.168.2.2",
            "Gi0/2": "192.168.3.1",
            "Gi0/3": "192.168.122.",
        }
        for intf in expected_ip.keys():
            try:
                found_intf = output.index(intf)
                found_ip = output[found_intf + 1]
                if expected_ip[intf] in found_ip:
                    print(f"{found_ip} of {intf} is assigned to VRF control-data")
                else:
                    print("Wrong IP")
            except Exception as e:
                print(e)
