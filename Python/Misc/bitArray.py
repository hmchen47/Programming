'''
Bit Arrays
URL: https://wiki.python.org/moin/BitArrays
'''
#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# pylint: disable=C0103

import array
import math

def makeBitArray(bitSize, fill=0):
    '''generate bit array'''
    intSize = bitSize >> 5  # number of 32 bit integer, using 32 bits as a unit
    if bitSize & 31:      # if bitSize != (32 * n) add
        intSize += 1      #   one more unit for stagglers

    if fill == 1:
        fill = 4294967295   # 2^32-> all bits filled
    else:
        fill = 0            # all bits cleared

    bitArray = array.array('I')         # generate a single char as base, 8 bits
    bitArray.extend((fill,) * intSize)

    return bitArray

def testBit(array_name, bit_num):
    '''returns a nonzero result, 2**offset, if the bit at 'bit-num' set to 1'''
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    return array_name[record] & mask

def setBit(array_name, bit_num):
    '''returns an integer with the bit at 'bit_num' set'''
    record = bit_num >> 5
    # offset = bit_num & 31
    # mask = 1 << offset
    return array_name[record]

def clearBit(array_name, bit_num):
    '''returns an integer with the bit at 'bit_num' cleared'''
    record = bit_num >> 5
    offset = bit_num & 31
    mask = ~(1 << offset)
    array_name[record] &= mask
    return array_name[record]

def toggleBit(array_name, bit_num):
    '''return an integer with bit at 'bit_num' inverted, 0-->1, 1-->0'''
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    array_name[record] ^= mask
    return array_name[record]

def primes(bits, ini):
    ''' get all primes with [1, bits] with the Sieve of Eratoshenes'''
    print("\nList of prime numbers below {}".format(bits))
    nmbrs = makeBitArray(bits, ini)

    # 0 & 1 are not prime, and not include in the Sieve of Eratoshenes
    bit = 0
    clearBit(nmbrs, bit)
    bit = 1
    clearBit(nmbrs, bit)

    for idx in range(int(math.sqrt(bits))):  # range is to "square root of limit"
        test = testBit(nmbrs, idx)

        if test:
            zeroBit = idx * idx # prime squared is lowest multiple left
            while zeroBit < bits:
                clearBit(nmbrs, zeroBit)
                zeroBit += idx

    cnt = 0
    for idx in range(bits):
        test = testBit(nmbrs, idx)
        if test:
            print(idx, end = ", ")
            cnt += 1

    print("\n\nTotal number of primes under {}: {}".format(bits, cnt))
    return

def main(bits, ini):
    ''' main function to control thw work flow'''
    myArray = makeBitArray(bits, ini)

    # array info: input bits; final length; excess bits, fill pattern
    print("bits= {}, length= {}, excess bits= {}, fill= {}".format(
        bits, len(myArray), (len(myArray) * 32) - bits, bin(myArray[0])
    ))

if __name__ == '__main__':
    BitSize = 15
    init = 1

    main(BitSize, init)
    # primes(BitSize, init)
