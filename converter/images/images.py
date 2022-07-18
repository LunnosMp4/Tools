#!/usr/bin/env python3
# Copyright (c) 2022, Lunnos
# https://github.com/LunnosMp4/Tools
# License: MIT

import sys, os
from PIL import Image

def images(input_file, ext):
    if not os.path.isfile(input_file):
        print("Input file is not a file or doesn't exist.")
        sys.exit(1)

    output = os.path.splitext(input_file)[0] + "_converted." + ext
    im = Image.open(input_file)
    rgb_im = im.convert('RGB')
    rgb_im.save(output)