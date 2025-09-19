from PIL import Image


def resize_image():
    img = Image.open("cleaned.bmp")

    # Resize the image to 1080x853
    img = img.resize((1280, 853), Image.NEAREST)

    img.save("cleaned.bmp", "BMP")

def formAChr(b1, b2, b3, b4, b5, b6, b7, b8):
    b1 = b1 & 0x01
    b2 = ((b2) & 0x02) >> 1
    b3 = b3 & 0x01
    b4 = ((b4) & 0x02) >> 1
    b5 = b5 & 0x01
    b6 = ((b6) & 0x02) >> 1
    b7 = b7 & 0x01
    b8 = ((b8) & 0x02) >> 1

    result = (b1 << 7) | (b2 << 6) | (b3 << 5) | (b4 << 4) | (b5 << 3) | (b6 << 2) | (b7 << 1) | b8

    # if (result < 36): result += 36

    #print(f"result: {result}")
    return result
    

if __name__ == "__main__":
    # Read from a file and put all hex in a string
    with open("sample.txt", "r") as file:
        str = file.read()

    # str = "66 5F 4C 64 5C 48 61 5F"

    # Convert the hex string to a list of integers
    hex_values = (int(x, 16) for x in str.split())
    hex_values = list(hex_values)
    # sample = "d7493c3e-8492-4624-b603-3e6a03a958"

    with open("output.txt", "wb") as output_file:
        for i in range(0, len(hex_values), 8):
            # Get the next 6 values
            if (i + 8) > len(hex_values):
                break
            b1 = hex_values[i]
            b2 = hex_values[i + 1]
            b3 = hex_values[i + 2]
            b4 = hex_values[i + 3]
            b5 = hex_values[i + 4]
            b6 = hex_values[i + 5]
            b7 = hex_values[i + 6]
            b8 = hex_values[i + 7]

            # Call formAChr with the 6 values
            result = formAChr(b1, b2, b3, b4, b5, b6, b7, b8)
            if (result == 0): continue

            # Convert result to a byte and write it directly
            output_file.write(bytes([result]))

            #print(f"result: {result}")

        

