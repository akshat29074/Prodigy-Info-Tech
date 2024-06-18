def caesar_cipher_encrypt(text, shift):
    """
    Encrypts the input text using the Caesar Cipher algorithm with the given shift.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    """
    Decrypts the input text using the Caesar Cipher algorithm with the given shift.
    """
    return caesar_cipher_encrypt(text, -shift)

def main():
    """
    Main function to run the Caesar Cipher encryption and decryption.
    """
    while True:
        print("Caesar Cipher Algorithm")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1' or choice == '2':
            message = input("Enter the message: ")
            try:
                shift = int(input("Enter the shift value: "))
            except ValueError:
                print("Shift value must be an integer. Try again.")
                continue

            if choice == '1':
                result = caesar_cipher_encrypt(message, shift)
                print(f"Encrypted message: {result}")
            elif choice == '2':
                result = caesar_cipher_decrypt(message, shift)
                print(f"Decrypted message: {result}")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
