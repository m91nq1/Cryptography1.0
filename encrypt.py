from cryptography.fernet import Fernet
import os

def generate_key(key_file):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as file:
        file.write(key)
    return key

def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_path, 'wb') as file:
        file.write(encrypted)

    print(f"File '{file_path}' has been encrypted.")

def main():
    key_file = 'secret.key'  
    code_file_path = r'D:\Bliss.txt'  

    # Create or load the key
    if os.path.exists(key_file):
        key = load_key(key_file)
    else:
        key = generate_key(key_file)

    # Encrypt the file
    if os.path.exists(code_file_path):
        encrypt_file(code_file_path, key)
    else:
        print(f"File '{code_file_path}' does not exist.")

if __name__ == "__main__":
    main()
