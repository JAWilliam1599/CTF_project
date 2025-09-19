# from pwn import *

# N = 100
# BITS = 6
# # pro = remote('chall.blackpinker.com', 33075)
# pro = process('./chall')  # Uncomment this line to run locally


# # Build the query contains 0 and 1 with length 100
# queries = []

# for k in range(BITS):  # 6 bits needed to represent 0..99
#     query = ""
#     for i in range(N):
#         bit = (i >> k) & 1
#         query += chr(bit+48)
#     queries.append(query)

# # # Print all queries
# # for idx, query in enumerate(queries):
# #     print(f"Query {idx}:")
# #     print("".join(map(str, query)))
# #     print()

# # context.log_level = 'debug'
# # pro = process('./chall')

# output = pro.recv(timeout=1)
# print("Got:", output.decode())

# outputs = []
# for idx, query in enumerate(queries):
#     pro.sendline(b'?')

#     try:
#         pro.sendline(query)
#         outputs.append(pro.recv(timeout=1).decode())

#     except EOFError:
#         print("Process exited early. Here's what it said:")
#         print(pro.recvall().decode())

# # Recover the permutation
# perm = [0] * N
# for j in range(N):
#     index = 0
#     for bit in range(BITS):
#         index |= (int(outputs[bit][j]) << bit)
#     perm[index] = j

# # Send the final answer
# pro.sendline(b'!')
# for val in perm:
#     pro.sendline(str(val).encode())

# # Interact to get the flag
# pro.interactive()
import random

N = 100
BITS = 6
perm = list(range(N))
random.shuffle(perm)
print("Secret permutation:", perm[:20], "...")

# Build 6 queries
queries = []
for bit in range(BITS):
    query = ''
    for i in range(N):
        query += str((i >> bit) & 1)
    queries.append(query)

# Simulate the ? responses
responses = []
for query in queries:
    response = ''.join(query[perm[i]] for i in range(N))
    responses.append(response)

# Recover the permutation
recovered = [0] * N
for j in range(N):
    index = 0
    for bit in range(BITS):
        index |= (int(responses[bit][j]) << bit)
    recovered[index] = j

print("Recovered perm:    ", recovered[:20], "...")
print("Correctly recovered:", recovered == perm)
