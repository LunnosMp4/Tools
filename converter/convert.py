#!/usr/bin/env python3
# Copyright (c) 2022, Lunnos
# https://github.com/LunnosMp4/Tools
# License: MIT

import sys
from converter.number.number import *
from converter.images.images import *
from converter.audio.audio import *

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

        # NUMBER CONVERTER
        if sys.argv[2] == "bin":
            return binary(getnb())
        if sys.argv[2] == "hex":
            return hexadecimal(getnb())
        if sys.argv[2] == "dec":
            return decimal(getnb())
        if sys.argv[2] == "oct":
            return octal(getnb())

        # IMAGE CONVERTER
        if sys.argv[2] == "jpg":
            return images(sys.argv[3], "jpg")
        if sys.argv[2] == "png":
            return images(sys.argv[3], "png")
        if sys.argv[2] == "jpeg":
            return images(sys.argv[3], "jpeg")
        if sys.argv[2] == "ico":
            return images(sys.argv[3], "ico")

        # AUDIO CONVERTER
        if sys.argv[2] == "mp3":
            return audio(sys.argv[3], "mp3")
        if sys.argv[2] == "wav":
            return audio(sys.argv[3], "wav")
        if sys.argv[2] == "flac":
            return audio(sys.argv[3], "flac")
        if sys.argv[2] == "ogg":
            return audio(sys.argv[3], "ogg")
        if sys.argv[2] == "m4a":
            return audio(sys.argv[3], "m4a")
        if sys.argv[2] == "aiff":
            return audio(sys.argv[3], "aiff")

        else:
            print("Command not found.")
    else:
        print("No command specified.")
        
