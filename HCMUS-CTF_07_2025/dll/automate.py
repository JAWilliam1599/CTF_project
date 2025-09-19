import hashlib
import pefile
from capstone import Cs, CS_ARCH_X86, CS_MODE_64

def hash_section(pe, section_name):
    for section in pe.sections:
        if section.Name.strip(b'\x00').decode() == section_name:
            return hashlib.md5(section.get_data()).hexdigest()
    return None

section_hashes = {}
for i in range(1000):
    path = f"{i:03}.dll"
    pe = pefile.PE(path)
    h = hash_section(pe, ".text")
    if h not in section_hashes:
        section_hashes[h] = []
    section_hashes[h].append(path)

for h, files in section_hashes.items():
    if len(files) < 1000:
        print(f"Sections: {h} → {files}")

# For every different section hash (except the first section), take out the PrintFlag section and take out the command that do sth
# mov eax, ... (the number to move is the character of the full flag)

# result = ""
# suspicious_dlls = [
#     "033.dll", "038.dll", "045.dll", "067.dll", "090.dll", "094.dll", "134.dll", "135.dll", "168.dll", "176.dll",
#     "196.dll", "226.dll", "235.dll", "240.dll", "276.dll", "438.dll", "439.dll", "496.dll", "530.dll", "581.dll", 
#     "625.dll", "626.dll", "634.dll", "677.dll", "690.dll", "707.dll", "758.dll", "786.dll", "788.dll", "878.dll",
#     "889.dll", "921.dll", "925.dll"
# ]
# for file in suspicious_dlls:
#     dll_path = f"./{file}"

#     try:
#         pe = pefile.PE(dll_path)
#         image_base = pe.OPTIONAL_HEADER.ImageBase

#         # Find the PrintFlag RVA
#         for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
#             if exp.name and exp.name == b"PrintFlag":
#                 va = exp.address
#                 rva = va
#                 break
#         else:
#             exit

#         # Convert RVA to file offset
#         offset = pe.get_offset_from_rva(rva)

#         # Read up to 50 bytes of code starting at that offset
#         code = pe.__data__[offset:offset + 50]

#         md = Cs(CS_ARCH_X86, CS_MODE_64)
#         instructions = list(md.disasm(code, image_base + rva))

#         for insn in instructions[:5]:
#             if insn.mnemonic == "mov" and insn.op_str.startswith("eax"):
#                 # take out the value
#                 value = insn.op_str.split(',')[-1]
#                 result += chr(int(value.strip(), 16))

#     except Exception as e:
#         print(f"[!] Error processing {dll_path}: {e}")
#         exit


#     print(result)


