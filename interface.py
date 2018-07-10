from RSA import encrypt, decrypt
import os

def right_path(file_path):
    if (file_path == ""):
        return file_path
    separate = file_path.split("\\")
    new = ""
    for temp in separate:
         new += temp + "\\"+"\\"
    return new

while(True):
    command = raw_input('Encrypt file or decrypt cipher?: ')
    if command.lower() == 'encrypt':
        file_path = raw_input('Include full file path: ')
        file_path = right_path(file_path)
        file_name = raw_input('Enter file name with extension: ')
        file_path += file_name
        encrypt(file_path)
        print("File successfully encrypted")
        break

    if command.lower() == 'decrypt':
        cipher_path = raw_input('Include full cipher path: ')
        cipher_path = right_path(cipher_path)
        file_name = raw_input('Enter file name with extension: ')
        cipher_path += file_name
        decrypt(cipher_path)
        print("Cipher successfully decrypted")
        break

    print("Wrong command, try again")
