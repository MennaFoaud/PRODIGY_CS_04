from PIL import Image
import numpy as np
import os

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    img = img.convert("RGB")  # Ensure image is in RGB mode

    # Convert the image to a numpy array
    img_array = np.array(img)
    
    # Encrypt the image by modifying pixel values
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            # Apply a simple encryption by modifying the RGB values with the key
            r, g, b = img_array[i, j]
            img_array[i, j] = (r ^ key, g ^ key, b ^ key)  # XOR each value with the key

    # Convert the numpy array back to an image
    encrypted_img = Image.fromarray(img_array)
    
    # Save the encrypted image
    encrypted_img.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}.")

def decrypt_image(encrypted_image_path, output_image_path, key):
    # Open the encrypted image
    img = Image.open(encrypted_image_path)
    img = img.convert("RGB")  # Ensure image is in RGB mode

    # Convert the image to a numpy array
    img_array = np.array(img)

    # Decrypt the image by reversing the pixel manipulation
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            # Reverse the encryption by XORing again with the same key
            r, g, b = img_array[i, j]
            img_array[i, j] = (r ^ key, g ^ key, b ^ key)

    # Convert the numpy array back to an image
    decrypted_img = Image.fromarray(img_array)

    # Save the decrypted image
    decrypted_img.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}.")

# Example usage:
input_image_path = r"C:\Users\menna\Desktop\flower.jpg"

if not os.path.exists(input_image_path):
    print(f"File not found: {input_image_path}")
else:
    print(f"File exists: {input_image_path}")  # Replace with your input image path
encrypted_image_path = "encrypted_example.png"
decrypted_image_path = "decrypted_example.png"
key = 123  # Key for encryption/decryption (must be the same for both operations)

# Encrypt the image
encrypt_image(input_image_path, encrypted_image_path, key)

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path, key)
