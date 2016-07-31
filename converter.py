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
from Crypto.Util.number import bytes_to_long, long_to_bytes
import os
import time

def converter(input_string):
    #accepts string
    lon = ""
    for i in input_string:
        if len(str(ord(i))) == 2:
            x = "0" + str(ord(i))
        elif len(str(ord(i))) == 3:
            x = str(ord(i))
        elif len(str(ord(i))) == 1:
            x = "00" + str(ord(i))
        lon = lon + x
    return long(lon)

#print converter("d")
#print converter("a")

def deconverter(input_long):
    in_string = str(input_long)
    if len(in_string) % 3 == 2:
        in_string = "0" + in_string
    elif len(in_string) % 3 == 1:
        in_string = "00" + in_string
    empt = []
    while len(in_string) != 0:
        thing = in_string[0] + in_string[1] + in_string[2]
        empt.append(thing)
        in_string = in_string[3:]
    end = ""
    for i in empt:
        end = end + chr(long(i))
    return end

print deconverter(97100)
