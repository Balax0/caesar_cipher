import numpy as np
import cv2

def process_image(image_path, key, output_path):
    """
    Encrypts or decrypts an image using XOR pixel manipulation.

    Parameters:
    image_path (str): Path to the image file.
    key (int): Encryption key (must be the same for encryption and decryption).
    output_path (str): Path to save the processed image.
    """
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Image not found or cannot be read.")

    # Convert image to a NumPy array
    image_array = np.array(image, dtype=np.uint8)

    # Apply XOR operation with the key to each pixel
    processed_array = image_array ^ key

    # Save the processed image
    cv2.imwrite(output_path, processed_array)
    print(f"Processed image saved as {output_path}")

    return output_path

# Get user input
image_path = input("Enter the image file path: ")
key = int(input("Enter the encryption/decryption key (integer): "))
mode = input("Enter mode (encrypt/decrypt): ").strip().lower()

# Define output file name
output_path = "encrypted.png" if mode == "encrypt" else "decrypted.png"

# Process image
process_image(image_path, key, output_path)


