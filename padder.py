thub'import math
import os
from Crypto.Util.number import bytes_to_long, long_to_bytes

def padder(n, converter_message):
    n_bin = str(bin(n))[2:]
    k_0_size = 128
    k_1_size = len(n_bin - 128)
    mess = n_bin + "0" * k_1_size
    r = str(bin(bytes_to_long(os.urandom(16))))[2:]
