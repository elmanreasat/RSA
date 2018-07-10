from GCDcalculator import gcd, modular_inverse
from ModExpo import modexp
from encoding import encode

private = open("private", "r")
public = open("public", "r")

private_keys = private.readlines()
public_keys = public.readlines()

priv_key = int (private_keys[1])
pub_key = int (public_keys[1])
n = int (private_keys[0])
message = 0
cipher = 0

def encrypt(filename):
	encoded_message = ""
	with open(filename) as file:
		for line in file:
			for word in line.split():
				message = encode(word)
				cipher = str(modexp(message, pub_key, n))
				encoded_message += cipher + "\r\n"
	cipher = open("cipher_text", "w+")
	cipher.write(encoded_message)	
	print("Success")	

encrypt("test.txt")