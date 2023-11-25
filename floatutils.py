def integerToBase(i, base, str_map='0123456789abcdefghijklmnopqrstuvwxyz'):
    if i < 0:
        return '-' + integerToBase(-i, base, str_map)

    s = ''
    while i > 0:
        s = str_map[i % base] + s
        i //= base
    return s


def floatToBase(f, base, decimalPoints=13, str_map='0123456789abcdefghijklmnopqrstuvwxyz'):
    new = integerToBase(int(f), base, str_map) + '.'

    from decimal import Decimal
    f = Decimal(f)
    m = f
    for i in range(decimalPoints):
        m *= base
        new += str_map[int(m) % base]
    return new


# convert a float to string without scientific notation

def floatToStr(f, base=10, decimalPoints=13, str_map='0123456789abcdefghijklmnopqrstuvwxyz'):
    return floatToBase(f, base, decimalPoints, str_map)


# returns a, b for f such that f = a * 2^b
# a, b are ints. f should be a float

def exactValueOfFloat(f):
    if f < 0:
        m, e = exactValueOfFloat(-f)
        return -m, e
    m, e = f.hex()[2:].split('p')
    e = 4 * (2 - len(m)) + int(e)
    m = int(m.replace('.', ''), 16)
    return m, e


def time_unique_id(base=16):
    import time
    f = time.time()
    f = f.hex()[2:].split('p')[0].replace('.', '')
    if base == 16:
        return f
    else:
        return integerToBase(int(f, 16))


def floatMantissa(f):
    return int(f.hex()[2:].split('p')[0].replace('.', ''), 16)


def mantissaExponentToFloat(m, e):
    return float.fromhex(hex(m) + 'p' + str(e))


def randomFloat():
    import struct
    import random
    import math
    while True:
        rf = struct.unpack('<d', random.getrandbits(64).to_bytes(8, 'little'))[0]
        if not math.isnan(rf):
            return rf


# the smallest float larger than f
def nextSmallestFloat(f):
    m, e = exactValueOfFloat(f)
    return mantissaExponentToFloat(m + 1, e)


# the largest float smaller than f
def previousLargestFloat(f):
    m, e = exactValueOfFloat(f)
    return mantissaExponentToFloat(m - 1, e)


def countUniqueItems(iterable, cmpfun=None):
    try:
        return len(set(iterable))
    except TypeError:  # unhashable type
        found = []
        if cmpfun is not None:
            for i in iterable:
                for j in found:
                    if cmpfun(i, j):
                        break  # i has already been found
                else:
                    found.append(i)
        else:
            for i in iterable:
                if i not in found:
                    found.append(i)
        return len(found)


def removeDuplicates(iterable, cmpfun=None):
    try:
        return list(set(iterable))
    except TypeError:  # unhashable type
        found = []
        if cmpfun is not None:
            for i in iterable:
                for j in found:
                    if cmpfun(i, j):
                        break  # i has already been found
                else:
                    found.append(i)
        else:
            for i in iterable:
                if i not in found:
                    found.append(i)
        return found

