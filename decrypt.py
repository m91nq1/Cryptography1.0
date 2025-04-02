from cryptography.fernet import Fernet
import os

def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted = file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(file_path, 'wb') as file:
        file.write(decrypted)

    print(f"File '{file_path}' has been decrypted.")

def main():
    key_file = 'secret.key'  
    encrypted_file_path = r'D:\Bliss.txt' 

    if os.path.exists(key_file):
        key = load_key(key_file)
    else:
        print("Key file not found. Cannot decrypt.")
        return

    # Decrypt the file
    if os.path.exists(encrypted_file_path):
        decrypt_file(encrypted_file_path, key)

        # Read and print decrypted content
        with open(encrypted_file_path, 'rb') as file:
            decrypted_content = file.read()
            print(f"Decrypted content: {decrypted_content.decode()}")
    else:
        print(f"File '{encrypted_file_path}' does not exist.")

if __name__ == "__main__":
    main()
