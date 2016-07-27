from pseudo_prime_check import powerMod
from pseudo_prime_check import isPrime
from pseudo_prime_check import isStrongPseudoprime
import random
import fractions
import uuid


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
    hexi = str(uuid.uuid4().hex)
    private_file_name = "Private_"+ hexi + ".txt"
    private_key = open(private_file_name, "w")
    private_key.write("Your private key d component =" + str(d))
    private_key.write("\n")
    private_key.write("YOur private key n component =" + str(n))
    private_key.close
    public_file_name = "Public_" + hexi + "txt"
    public_key = open(public_file_name, "w")
    public_key.write("Your public key e component =" + str(e))
    public_key.write("\n")
    public_key.write("Your public key n component =" + str(n))
    public_key.close
    return (public_file_name, private_file_name)
