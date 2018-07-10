from GCDcalculator import gcd, modular_inverse, mod
from LargePrimeGen import generate_prime_number
from random import randrange, getrandbits
import math
from ModExpo import modexp

def generate_d():
	d = getrandbits(32)
	while(gcd(d, (P-1)*(Q-1)) != 1):
		d = getrandbits(32)

	return d


P = generate_prime_number()
Q = generate_prime_number()
n = P*Q
d = generate_d()
k = getrandbits(32)
e = modular_inverse(d, (P-1)*(Q-1))
f = modular_inverse(e, (P-1)*(Q-1))

C = modexp(13, e, n)
M = modexp(C, d, n)

print(C)
print(M)