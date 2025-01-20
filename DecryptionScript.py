#Disclaimer: This script is for educational purposes only and should not be used for malicious activities.
import os
from cryptography.fernet import Fernet
# Load the encryption key
def load_key():
    try:
        with open("encryption.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Error: encryption.key file not found. Ensure it's in the same directory as this script.")
        exit()
# Decrypt a single file
def decrypt_file(file_path, key):
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = Fernet(key).decrypt(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(decrypted_data)
        print(f"Decrypted: {file_path}")
    except Exception as e:
        print(f"Failed to decrypt {file_path}: {e}")
# Decrypt all files in a directory
def decrypt_directory(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Skip the ransom note and key files
            if file == "RANSOM_NOTE.txt" or file == "encryption.key":
                continue
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)
# Main function
def main():
    # Target directory (same directory used for encryption)
    target_directory = "C:\\Users\\vboxuser\\Desktop\\RansomwareTest"
    # Load the encryption key
    key = load_key()
    print("Encryption key loaded.")
    # Decrypt files in the target directory
    decrypt_directory(target_directory, key)
    print("Decryption completed. All files have been restored.")

if __name__ == "__main__":
    main()
