#!/usr/bin/python3
import pickle
import sys
import string

mem = []

def VM(data, countFind):
    with open("image.bin", "rb") as f:
        mem = pickle.load(f)

    count = 0

    mem[60001:60017] = data
        
    while True:
        if mem[4] == 1:
            # print("DONE")
            break
        i = mem[0]
        a1 = mem[i]
        a2 = mem[i + 1]
        a3 = mem[i + 2]
        
        tmp = (~(mem[a1] | mem[a2])) & 0xffff
        
        if(a3 == 60100 and tmp == 0 and count != countFind):
            count += 1
        elif (a3 == 60100 and tmp == 0):
            return 1

        mem[a3] = tmp
        mem[1] = ((tmp >> 15) & 1) | ((tmp & 0x7FFF) << 1) # Shift left with 1 added
        mem[0] = i + 3
    
    with open("after.txt", "w") as f:
        # Write the whole mem
        for i in mem:
            f.write(f"{i:04x}\n")
    return 0

key = b"\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01"
find = ""
for k in range(16):
    for i in range(32, 128):
        payload = find.encode() + bytes([i]) + key

        if(VM(payload, len(find)) == 1):
            find += chr(i)
            key = key[:-1]
            break

    print(find)

# if not (len(key) == 16):
#     print("Incorrect format!")
#     sys.exit(1)

# if VM(key) == 0:
#     print("Correct!, wraps your key with HCMUS-CTF{}")
# else:
#     print("Incorrect key!")