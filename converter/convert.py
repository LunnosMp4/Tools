#!/usr/bin/env python3
# Copyright (c) 2022, Lunnos
# https://github.com/LunnosMp4/Tools
# License: MIT

import sys

# NUMBER CONVERTER
def getnb():
    if len(sys.argv) == 4:
        nb = sys.argv[3]
        return nb
    nb = input("Enter an input : ")
    return nb

def binary(nb):
    #TODO : check if nb is a binary number
    base = int(nb, 2)
    print("Hexadecimal :", hex(base))
    print("Octal :", oct(base))
    print("Decimal :", (int(base)))

def hexadecimal(nb):
    #TODO : check if nb is a hexadecimal number
    base = int(nb, 16)
    print("Binary : " + bin(base))
    print("Octal : " + oct(base))
    print("Decimal : " + base)

def decimal(nb):
    #TODO : check if nb is a decimal number
    base = int(nb, 10)
    print("Binary : " + bin(base))
    print("Hexadecimal : " + hex(base))
    print("Octal : " + oct(base))

def octal(nb):
    #TODO : check if nb is a octal number
    base = int(nb, 8)
    print("Binary : " + bin(base))
    print("Hexadecimal : " + hex(base))
    print("Decimal : " + base)


def convert():
    if len(sys.argv) >= 3 and len(sys.argv) <= 4:
        if sys.argv[2] == "bin":
            return binary(getnb())
        elif sys.argv[2] == "hex":
            return hexadecimal(getnb())
        elif sys.argv[2] == "dec":
            return decimal(getnb())
        elif sys.argv[2] == "oct":
            return octal(getnb())
        else:
            print("Command not found.")
    else:
        print("No command specified.")
        
