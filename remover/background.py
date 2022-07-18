#!/usr/bin/env python3
# Copyright (c) 2022, Lunnos
# https://github.com/LunnosMp4/Tools
# License: MIT

import sys, torch
# from rembg.bg import remove

def background():
    if len(sys.argv) < 4:
        print("Usage: remove bg <file>")
        sys.exit(1)
    # input_path = sys.argv[3]
    # output_path = os.path.splitext(input_path)[0] + "_transparent.png"

    # with open(input_path, 'rb') as i:
    #     with open(output_path, 'wb') as o:
    #         input = i.read()
    #         output = remove(input)
            # o.write(output)