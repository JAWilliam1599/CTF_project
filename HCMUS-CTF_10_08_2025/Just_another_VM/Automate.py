import pexpect as p

path = "/home/minh/CTF/start"

for i in range(10, 21):  # try from 0 to 9, or more
    print(f"Trying machine id {i}")
    child = p.spawn(path, ["-m", str(i)])
    try:
        child.expect("Key:", timeout=5)
        child.sendline("asdasdasdasdasd")
        index = child.expect(["IncorrectMachine halting!", p.EOF, p.TIMEOUT], timeout=5)
        if index == 0:
            print(f"Machine {i}: IncorrectMachine halting!")
        else:
            print(f"Machine {i}: No incorrect message, possible success!")
            print(child.before.decode())
            break
    except p.exceptions.TIMEOUT:
        print(f"Machine {i}: Timeout waiting for prompt")
    child.close()
