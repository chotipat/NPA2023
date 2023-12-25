# pylint: disable=invalid-name
# pylint: disable=missing-module-docstring
import getpass
import telnetlib
import time

HOST = "172.31.129.3"
# user = input("Enter your remote account: ")
# password = getpass.getpass()
password = "cisco"

tn = telnetlib.Telnet(HOST, 23, 5)

tn.read_until(b"Username:")
tn.write(user.encode("ascii") + b"\n")
time.sleep(1)

if password:
    tn.read_until(b"Password:")
    tn.write(password.encode("ascii") + b"\n")
    time.sleep(1)

tn.write(b"configure terminal\n")
time.sleep(2)
tn.write(b"int g0/1\n")
time.sleep(2)
tn.write(b"vrf forwarding control-data\n")
time.sleep(2)
tn.write(b"ip add 192.168.1.1 255.255.255.0\n")
time.sleep(2)
tn.write(b"no shut\n")
time.sleep(2)
tn.write(b"exit\n")
time.sleep(2)
tn.write(b"int g0/2\n")
time.sleep(2)
tn.write(b"vrf forwarding control-data\n")
time.sleep(2)
tn.write(b"ip add 192.168.2.1 255.255.255.0\n")
time.sleep(2)
tn.write(b"no shut\n")
time.sleep(2)
tn.write(b"end\n")
time.sleep(2)
tn.write(b"show ip vrf interfaces control-data\n")
time.sleep(2)

output = tn.read_very_eager()
output = output.decode("ascii")
output = output.split()
expected_ip = {"Gi0/1": "192.168.1.1", "Gi0/2": "192.168.2.1"}
for intf in expected_ip.keys():
    try:
        found_intf = output.index(intf)
        found_ip = output[found_intf + 1]
        if found_ip == expected_ip[intf]:
            print(f"{found_ip} of {intf} is assigned to VRF control-data")
        else:
            print("Wrong IP.")
    except Exception as e:
        print(e)

tn.close()
