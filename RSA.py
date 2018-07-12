from GCDcalculator import gcd, modular_inverse, modexp
from encoding import encode, decode

private = open("private", "r")
public = open("public", "r")

private_keys = private.readlines()
public_keys = public.readlines()

priv_key = int (private_keys[1])
pub_key = int (public_keys[1])
n = int (private_keys[0])
message = 0
cipher = 0

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def encrypt(filename):
	encoded_message = ""
	with open(filename) as file:
		for word in file.read().split():
			message = encode(word)
			cipher = str(modexp(message, pub_key, n))
			encoded_message += cipher + "\r\n"
	cipher = open("cipher_text", "w+")
	cipher.write(encoded_message)		


def decrypt(filename):
	original_message = ""
	
	file = open(filename, "r")
	letters = file.readlines()
	i = 0
	length = file_len(filename)

	while(i < length):
		cipher = letters[i]
		message = str(modexp(int(cipher), priv_key, n))
		original_message += decode(message) + " "
		i = i + 1

	decoded_message = open("decoded_message.txt", "w+")
	decoded_message.write(original_message)		

