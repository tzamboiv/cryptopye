from pseudo_prime_check import powerMod
from pseudo_prime_check import isPrime
from pseudo_prime_check import isStrongPseudoprime
import random
import fractions


def prime_maker(a, k):
#k corresponds to degree of certainty that this output is prime
    x = random.randint(10**a, 10**(a+1))
    while isPrime(x, k) == "Composite":
        x = random.randint(10**a, 10**(a+4))
    return x

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return(g, y - (b // a)*x, x)
def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def key_maker(a, k):
    p = prime_maker(a, k)
    q = prime_maker(a, k)
    n = p * q
    totient = (p-1)*(q-1)
    e = random.randint(2, totient)
    while fractions.gcd(e, totient) != 1:
        e = random.randint(2, totient)
    d = mulinv(e, totient)
    private_key = open("private_key.txt", "w")
    private_key.write(str(d))
    private_key.close
    return e
print key_maker(100, 15)
