from GCDcalculator import gcd, modular_inverse
from LargePrimeGen import generate_prime_number
from random import randrange, getrandbits


private = open("private", "w+")
public = open("public", "w+")

def generate_d():
	d = getrandbits(1024)
	while(gcd(d, (P-1)*(Q-1)) != 1):
		d = getrandbits(1024)

	return d

P = generate_prime_number() #random large prime 1
Q = generate_prime_number() #random large prime 2
n = P*Q
priv_key = generate_d()
pub_key = modular_inverse(d, (P-1)*(Q-1))

private.write(str(n) + "\r\n")
private.write(str(priv_key) + "\r\n")
public.write(str(n) + "\r\n")
public.write(str(pub_key) + "\r\n")

print("Success")