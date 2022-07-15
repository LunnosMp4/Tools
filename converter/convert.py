#!/usr/bin/env python3
# Copyright (c) 2022, Lunnos
# https://github.com/LunnosMp4/Tools
# License: MIT

import sys
from converter.number.number import *
from converter.images.images import *

def help():
    return print("""
    Convert a number to another base.
    Usage:
        -cvt <base> <number>
        --convert <base> <number>
        (base : bin, hex, dec, oct)
    
    Convert an image to another format.
    Usage:
        -cvt <format> <image>
        --convert <format> <image>
        (format : jpg, png, jpeg, ico)
    """)

def convert():
    if len(sys.argv) >= 3 and len(sys.argv) <= 4:
        if sys.argv[2] == "-h" or sys.argv[2] == "--help":
            return help()
        if sys.argv[2] == "bin":
            return binary(getnb())
        if sys.argv[2] == "hex":
            return hexadecimal(getnb())
        if sys.argv[2] == "dec":
            return decimal(getnb())
        if sys.argv[2] == "oct":
            return octal(getnb())
        if sys.argv[2] == "jpg":
            return images(sys.argv[3], "jpg")
        if sys.argv[2] == "png":
            return images(sys.argv[3], "png")
        if sys.argv[2] == "jpeg":
            return images(sys.argv[3], "jpeg")
        if sys.argv[2] == "ico":
            return images(sys.argv[3], "ico")

        else:
            print("Command not found.")
    else:
        print("No command specified.")
        
