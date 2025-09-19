import zlib

file = './reconstruct_git/.git/objects/pack/c1edf5ae097edd6153379cf537d33a71a6b22718.pack.enc'
with open(file, 'rb') as f:
    data = f.read()
    
    # Split to 1 byte and XOR with 0x1D
    data = bytes([b ^ 0x1D for b in data])

    # Write back to a new file name the same as the original but without .enc
    new_file = file.replace('.enc', '')
    with open(new_file, 'wb') as f:
        f.write(data)