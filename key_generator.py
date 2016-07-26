from pseudo_prime_check import powerMod
from pseudo_prime_check import isPrime
from pseudo_prime_check import isStrongPseudoprime
import random

def prime_maker(a,b, k):
#k corresponds to degree of certainty that this output is prime
    x = random.randint(a, b)
    while isPrime(x, k) == "Composite":
        x = random.randint(a, b)
    return x
print prime_maker(1000, 10000, 4)
