def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():  # Process only letters
            is_upper = char.isupper()
            base = ord('A') if is_upper else ord('a')

            if mode == "encrypt":
                new_char = chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                new_char = chr((ord(char) - base - shift) % 26 + base)
            result += new_char
        else:
            result += char  # Keep spaces and symbols unchanged

    return result


# User input
message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))
choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

if choice in ["encrypt", "decrypt"]:
    output = caesar_cipher(message, shift_value, choice)
    print(f"Result: {output}")
else:
    print("Invalid choice! Please type 'encrypt' or 'decrypt'.")
