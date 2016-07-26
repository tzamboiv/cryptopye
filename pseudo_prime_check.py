import random
import math

def powerMod(b, e, m):
    x = 1
    while e > 0:
        if e % 2 == 1:
            x = (b * x) % m
        b = (b * b) % m
        e = e // 2
    return x
def isStrongPseudoprime(n, a):
    d = n-1
    s = 0
    while d % 2 == 0:
        d = d / 2
        s = s + 1
    t = powerMod(a, d, n)
    if t == 1:
        return "Probably Prime"
    while s > 0:
        if t == n-1:
            return "Probably Prime"
        t = (t*t)%n
        s = s - 1
    return "Composite"
def isPrime(n, k):
    for i in (1,k):
        a = random.randint(2, n-1)
        if isStrongPseudoprime(n, a) == "Composite":
            return "Composite"
    return "Probably Prime"
semi = math.factorial(38) + 1
print isPrime(semi, 2)
