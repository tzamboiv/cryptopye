from pseudo_prime_check import powerMod
from pseudo_prime_check import isPrime
from pseudo_prime_check import isStrongPseudoprime
import random
import fractions
import uuid
import math
from key_generator import key_maker
from key_generator import egcd
from key_generator import mulinv
from key_generator import prime_maker

def encryptor(n,e, plain_num):
    #encrypts an integer using e, the public key, and n
    ciphertext = pow(plain_num, e, n)
    return ciphertext
def decryptor(n, d, ciph_num):
    #decrypts an integer using d, the private key, and n
    plaintext = pow(ciph_num, d, n)
    return plaintext
a = int(input("Enter n"))
b = int(input("Enter e"))
c = 1234
ciph = encryptor(a, b, c)
print encryptor(a, b, c)
d = int(input("Enter d"))
print decryptor(a, d, ciph)
