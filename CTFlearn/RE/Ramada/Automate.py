# From ! to ~, take the string, turn to int, then cube and turn to hex, pad to 8 digits
character_int_map = {'0x' + hex(i * i * i)[2:].zfill(8) : chr(i) for i in range(33, 127)}

input = \
"0x00013693, 0x0006b2c0, 0x0011a9f9, 0x00157000, " \
"0x0001cb91, 0x001bb528, 0x001bb528, 0x000ded21, " \
"0x00144f38, 0x000fb89d, 0x00169b48, 0x000d151f, " \
"0x0008b98b, 0x0017d140, 0x000ded21, 0x001338c0, "\
"0x001338c0, 0x0011a9f9, 0x0001b000, 0x00144f38, "\
"0x001734eb"

input_list = input.split(", ")
output = ''
# loop through the list, map to character_int_map, and join the characters
for i in input_list:
    # Convert hex string to int, then to character using the map, find its value and get the key
    char = character_int_map.get(i, '?')  # Use '?' for unmapped characters
    output += char

print(output)