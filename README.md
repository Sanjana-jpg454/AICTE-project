Overview

This project demonstrates a basic steganography technique where a secret message is embedded into an image by modifying pixel values. The message can later be retrieved using a passcode.

Prerequisites

Ensure you have the following installed:

Python 3.x

OpenCV (cv2)

Install OpenCV using:

pip install opencv-python

How It Works

The user provides a secret message and a passcode.

The message is encoded into the image by modifying pixel values.

The modified image is saved as encryptedImage.jpg.

To retrieve the message, the user enters the correct passcode.

The program extracts and displays the original message if the passcode matches.

Code

import cv2
import os

# Read the image
img = cv2.imread("WIN_20230213_14_36_00_Pro.jpg")  # Replace with the correct image path

# Get user inputs
msg = input("Enter secret message:")
password = input("Enter a passcode:")

d = {}
c = {}

# Create encoding and decoding dictionaries
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m, n, z = 0, 0, 0

# Encode message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3

# Save the modified image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Opens the image (Windows only)

# Decryption
message = ""
n, m, z = 0, 0, 0
pas = input("Enter passcode for Decryption: ")

if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")

Limitations

The encoding method directly modifies pixel values, making it detectable.

Poor error handling: If the message is too long, it may exceed image dimensions.

Security issues: The message is stored in plaintext in the image pixels.

Potential Improvements

Use Least Significant Bit (LSB) Steganography: Embed message bits into the least significant bits of pixel values to minimize visual changes.

Enhance Security: Encrypt the message before encoding.

Improve Pixel Traversal: Ensure the message fits within the image dimensions properly.

Usage

Run the script and follow the prompts to enter your message and passcode.

python steganography.py

The encoded image will be saved as encryptedImage.jpg. Enter the correct passcode to retrieve the message.

Feel free to contribute and improve this project! 
