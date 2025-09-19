
set -x
nasm -f elf64 -F dwarf -o Raspberry.o Raspberry.asm
nasm -f elf64 -F dwarf -o Strings.o Strings.asm
nasm -f elf64 -F dwarf -o Utils.o Utils.asm

ld Raspberry.o Strings.o Utils.o -o Raspberry

set +x

chmod +x Raspberry
./Raspberry
echo $?
