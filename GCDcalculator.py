def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)    


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def modular_inverse(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m

# Function to compute num (mod a)
def mod(num, a):
     
    # Initialize result
    res = 0
 
    # One by one process all digits
    # of 'num'
    for i in range(0, len(num)):
        res = (res * 10 + int(num[i])) % a;
 
    return res

def modexp(a, b, n):
    r = 1
    for bit in reversed(bits_of_n(b)):
        r = r * r % n
        if bit == 1:
            r = r * a % n
    return r

def bits_of_n(n):
    bits = []
    while n:
        bits.append(n % 2)
        n /= 2
    return bits
