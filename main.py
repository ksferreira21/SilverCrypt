import json
from packet.interface import *
from time import sleep
from packet.cryptography import *
from packet.drive_sync import upload_to_drive

# Load the encryption key
key = load_key()
print(f"The loaded key is: {key.decode()}")

while True:
    response = menu(['View your passwords', 'Register a new password', 'Exit the system'])
    
    if response == 1:
        passwords = load_passwords()
        if not passwords:
            print("No passwords registered.")
        else:
            for service, encrypted_password in passwords.items():
                decrypted_password = decrypt(encrypted_password.encode(), key)
                print(f"Service: {service} | Password: {decrypted_password}")

    elif response == 2:
        service = input("What service is this password for? ")
        password = input("Password: ")
        encrypted_password = encrypt(password, key)
        save_password(service, encrypted_password)
        print(f"Password for {service} encrypted and saved!")
        upload_to_drive("passwords.json", "passwords.json")

    elif response == 3:
        text('Come back anytime!')
        break

    else:
        print('\033[1;31mError: Please enter a valid integer!\033[m')

    sleep(2)

