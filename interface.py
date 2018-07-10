from RSA import encrypt, decrypt
import os

print()

while(True):
    command = raw_input('Encrypt file or decrypt cipher?: ')
    if command.lower() == 'encrypt':
        file_path = raw_input('Include full file path: ')
        print(file_path)
        encrypt(file_path)
        print("File encrypted successfully")
        break

    if command.lower() == 'decrypt':
        cipher_path = raw_input('Include full cipher path: ')
        decrypt(cipher_path)
        print("Cipher decrypted successfully")
        break

    print("try again")
