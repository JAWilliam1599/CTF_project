
# Add 4 to each character in the string
# The string is a sequence of characters

sample = "D?IQO)?PBwjks[u,q[gjks[pd/[=NI[jkp[FqOP[t42y"

shifted = ''.join(chr(ord(c) + 4) for c in sample)

print(shifted)