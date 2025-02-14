import os
from cryptography.fernet import Fernet
import json

PASSWORD_FILE = "passwords.json"
KEY_FILE = "key.key"

# Function to generate and save a new encryption key
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key

# Function to load the encryption key from file or generate a new one if it does not exist
def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        return generate_key()

# Function to save an encrypted password for a specific service
def save_password(service, encrypted_password):
    passwords = load_passwords()
    passwords[service] = encrypted_password.decode()
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)

# Function to load all stored passwords from file
def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to encrypt a message
def encrypt(msg, key):
    f = Fernet(key)
    encrypted_msg = f.encrypt(msg.encode())
    return encrypted_msg

# Function to decrypt a message
def decrypt(encrypted_msg, key):
    f = Fernet(key)
    decrypted_msg = f.decrypt(encrypted_msg).decode()
    return decrypted_msg

