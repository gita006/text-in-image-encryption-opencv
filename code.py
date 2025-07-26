import cv2
import string
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow  # for image display in Colab

# Character encoding and decoding
d = {}
c = {}
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Load the image
x = cv2.imread("makeup.jpg")
if x is None:
    print("Image not found. Please upload 'makeup.jpg' to Colab.")
    exit()

height, width = x.shape[0], x.shape[1]
print("Image dimensions:", height, width)

# Get inputs
key = input("Enter key to edit (Security Key): ")
text = input("Enter text to hide: ")

kl = 0
text_len = len(text)

# Position and channel tracking
n = 0
m = 0
z = 0

# Hide the text
for i in range(text_len):
    if n >= height:
        print("Message too long for this image. Truncating.")
        break

    x[n, m, z] = d[text[i]] ^ d[key[kl]]
    kl = (kl + 1) % len(key)

    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= width:
            m = 0
            n += 1

# Save the new image
cv2.imwrite("makeup_encrypted.jpg", x)

# Show the image inside Colab
print("✅ Encrypted image preview:")
cv2_imshow(x)

# Ask if user wants to extract
ch = int(input("\nEnter 1 to extract data from Image: "))
if ch == 1:
    key1 = input("Re-enter key to extract text: ")
    decrypt = ""

    if key == key1:
        kl = 0
        n = 0
        m = 0
        z = 0

        for i in range(text_len):
            if n >= height:
                break

            decrypt += c[x[n, m, z] ^ d[key[kl]]]
            kl = (kl + 1) % len(key)

            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m >= width:
                    m = 0
                    n += 1

        print("🔓 Encrypted text was:", decrypt)
    else:
        print("❌ Key doesn't match.")
else:
    print("Thank you. Exiting.")
