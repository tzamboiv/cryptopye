import random
import math

#This is pseudo_prime_check. This program checks to a specified degree of accuracy whether or not a large number is prime. It is part of the cyptopye projec ton github.
    #Copyright (C) 2016  Edward "Teddy" Zamborsky

    #This program is free software: you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the GNU General Public License
    #along with this program.  If not, see <http://www.gnu.org/licenses/>.
    #Contact the author by email at tzamboiv@gmail.com (Public key is available online) or on twitter @tzamboiv

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
