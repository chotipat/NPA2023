import pexpect


def configure():
    prompt = "#"
    router_id = [1, 2]
    routers_ip = ["172.31.129.3", "172.31.129.4"]
    username = "admin"
    password = "cisco"
    commands = ["conf t", "int lo0", "ip add ", "no shut", "end"]
    test_command = "sh ip int bri"

    for rid, rip in zip(router_id, routers_ip):
        loopback_ip = f"172.16.{rid}.{rid}"
        child = pexpect.spawn("telnet " + rip)
        child.expect("Username")
        child.sendline(username)
        child.expect("Password")
        child.sendline(password)
        for command in commands:
            child.expect(prompt)
            if command == "ip add ":
                command = command + loopback_ip + " 255.255.255.255"
            child.sendline(command)
        child.expect(prompt)
        child.sendline(test_command)
        child.expect(prompt)
        result = child.before
        expected_result = ["Loopback0", loopback_ip]
        success = test(result, expected_result)
        if success:
            print(f"{expected_result[0]} {expected_result[1]} is created on {rip}")
        else:
            print(f"Fail to create {expected_result[0]} {expected_result[1]} on {rip}")
        child.sendline("exit")
        child.close()


def test(result, expected_result):
    result = result.decode("UTF-8")
    result_list = result.split("\n")
    success = False
    for result in result_list:
        if len(result.split()) == 6:
            interface, ip_address, ok, method, status, protocol = result.split()
            if interface == expected_result[0] and ip_address == expected_result[1]:
                success = True
    return success


configure()
