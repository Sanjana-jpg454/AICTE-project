import cv2
import os

# Load the original image
img = cv2.imread("WIN_20230213_14_36_00_Pro.jpg")  # Replace with correct path
original_img = img.copy()  # Store a copy of the original image

# User inputs
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Create encoding and decoding mappings
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Encode message into the image
m, n, z = 0, 0, 0
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Opens image on Windows

# Decryption Process
message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    print("Decrypted message:", message)
    
    # Restore the original pixel values
    decrypted_img = original_img.copy()
    cv2.imwrite("decryptedImage.jpg", decrypted_img)  # Save decrypted image
    os.system("start decryptedImage.jpg")  # Open decrypted image on Windows
else:
    print("YOU ARE NOT AUTHORIZED")
