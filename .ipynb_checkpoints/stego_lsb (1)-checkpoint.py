# ---------------------------------------------------------
# Image Steganography using LSB (Least Significant Bit)
# Idea: hide secret text in the LAST bit of every colour value.
# Changing the last bit changes a colour by only 1 (out of 255),
# so the human eye cannot see any difference.
# ---------------------------------------------------------

from PIL import Image   # Pillow library to open/save images (pip install pillow)

END = "#"   # special character that tells us where the secret message ends


def hide(cover_path, output_path, message):
    # 1. Open the normal (cover) image and make sure it has R, G, B colours
    img = Image.open(cover_path).convert("RGB")

    # 2. Convert the message to bits. Example: "A" -> 65 -> "01000001"
    #    ord(ch) gives the number of the letter, "08b" makes it 8 binary digits.
    #    We add END at the end so we know where to stop while reading.
    bits = "".join(format(ord(ch), "08b") for ch in message + END)

    # 3. Take all pixels and put every colour number in one flat list.
    #    A pixel is (R, G, B), so 2 pixels give [R1, G1, B1, R2, G2, B2]
    values = [v for pixel in img.getdata() for v in pixel]

    # 4. Put one secret bit into the last bit of each colour number
    for i, bit in enumerate(bits):
        # (values[i] & ~1) -> makes the last bit 0
        # | int(bit)       -> puts our secret bit (0 or 1) there
        values[i] = (values[i] & ~1) | int(bit)

    # 5. Build a new image from the changed numbers
    stego = Image.new("RGB", img.size)
    # zip(*[iter(values)] * 3) groups the flat list back into (R, G, B)
    stego.putdata(list(zip(*[iter(values)] * 3)))

    # 6. Save as PNG. Never use JPG: it compresses and destroys the hidden bits
    stego.save(output_path)


def reveal(stego_path):
    # 1. Open the image that has the hidden message
    img = Image.open(stego_path).convert("RGB")

    # 2. Read the LAST bit of every colour number (v & 1 gives the last bit)
    bits = "".join(str(v & 1) for pixel in img.getdata() for v in pixel)

    # 3. Take 8 bits at a time and turn each group back into a letter
    #    int(group, 2) converts binary to a number, chr() converts it to a letter
    text = "".join(chr(int(bits[i:i + 8], 2)) for i in range(0, len(bits) - 7, 8))

    # 4. Keep only the part before the END marker, that is our secret message
    return text.split(END)[0]


# ---------------- Demo ----------------
hide("cover.png", "secret.png", "Meet me at 5 PM")   # hide the message
print("Hidden message:", reveal("secret.png"))        # read it back
