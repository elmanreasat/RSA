# RSA Implementation
RSA is a public-key cryptosystems and is widely used for secure data transmission. The encryption key is public and it is different from the decryption key which is kept secret (private). In RSA, this asymmetry is based on the practical difficulty of the factorization of the product of two large prime numbers, the "factoring problem". Source: [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)).
Implementation of RSA is achieved through generation of large primes using [Miller-Rabin Primality Test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test).
Computation of large exponents is achieved through [Modular Exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation).
## Setup
```sh
$ git clone https://github.com/elmanreasat/RSA.git
$ cd RSA
$ make
```
**Encrypt**
```sh
> Encrypt file or decrypt cipher?: encrypt
> Include full file path: <file path>
> Enter file name with extension: <file name>  # i.e. myfile.txt
> File successfully encrypted
```
**Decrypt**
```sh
> Encrypt file or decrypt cipher?: decrypt
> Include full cipher path: <use dir path to rsa repo>
> Enter file name with extension: cipher_text # encrypted messaged stored here
> Cipher successfully decrypted
```
## Author
Elman Reasat [@elmanreasat](https://www.github.com/elmanreasat)
## License
MIT License

## Limitations
Encryption only works for lowercase letters.
