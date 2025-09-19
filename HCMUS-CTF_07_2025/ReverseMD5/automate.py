hint   = bytes.fromhex("14aab2f8649b8af59e5b10f59d2f03b3")
memory = bytes.fromhex("68607fcb6ffb4feef431032496f5b3b5")

# XOR the two
xor = bytes([a ^ b for a, b in zip(hint, memory)])

# print the result as string
print(xor.decode('utf-8', errors='ignore'))
