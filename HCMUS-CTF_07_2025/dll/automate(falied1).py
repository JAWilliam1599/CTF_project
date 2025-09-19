import pefile
from capstone import *
import hashlib
import os

# The exact stub instruction pattern
STUB_PATTERN = [
    ("push", "rbp"),
    ("mov", "rbp, rsp"),
    ("mov", "eax, 0"),
    ("pop", "rbp"),
    ("ret", ''),
]

def is_stub(instructions):
    """Check if the instructions exactly match the stub pattern"""
    if len(instructions) < 5:
        return False

    # Get the first 5 mnemonics and operands
    sequence = []
    for insn in instructions[:5]:
        if insn.mnemonic == "mov" and insn.op_str.startswith("eax"):
            op = "eax, 0"
        else:
            op = insn.op_str
        sequence.append((insn.mnemonic, op))
        
    return sequence == STUB_PATTERN


def disasm_printflag(dll_path):
    try:
        pe = pefile.PE(dll_path)
        image_base = pe.OPTIONAL_HEADER.ImageBase

        # Find the PrintFlag RVA
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            if exp.name and exp.name == b"PrintFlag":
                va = exp.address
                rva = va
                break
        else:
            return False

        # Convert RVA to file offset
        offset = pe.get_offset_from_rva(rva)

        # Read up to 50 bytes of code starting at that offset
        code = pe.__data__[offset:offset + 50]
        if not code:
            return False
        if len(code) < 5:
            return False

        md = Cs(CS_ARCH_X86, CS_MODE_64)
        instructions = list(md.disasm(code, image_base + rva))

        if is_stub(instructions):
            return False  # it's the known stub
        return True

    except Exception as e:
        print(f"[!] Error processing {dll_path}: {e}")
        return False

for i in range(1000):
    if disasm_printflag(f"./{i:03}.dll"):
        print(f"Found PrintFlag in {i:03}.dll")


# They are all unique, so we need to check each dll that has more than 5-6 instructions
# def check_delete_duplicates():
#     """
#     Check for duplicate DLL files based on their SHA-256 hash.
#     If a duplicate is found, it will be deleted.
#     """

#     hash_list = []

#     with open("./000.dll", 'rb') as f:
#         content = f.read()
#         hash_value = hashlib.sha256(content).hexdigest()
#         hash_list.append(hash_value)


#     for i in range(1, 1000):
#         dll_name = f"./{i:03}.dll"
        
#         # Check for duplicates with the first DLL
#         with open(dll_name, 'rb') as f:
#             content = f.read()
#             current_hash = hashlib.sha256(content).hexdigest()
            
#             if current_hash in hash_list:
#                 print(f"Duplicate found: {dll_name} is identical to a previous DLL. Deleting {dll_name}.")
#                 os.remove(dll_name)
#             else:
#                 print(f"{dll_name} is unique, adding its hash to the list.")
#                 hash_list.append(current_hash)