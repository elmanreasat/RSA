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
