#!/usr/bin/env python3
# Copyright (c) 2022, Lunnos
# https://github.com/LunnosMp4/Tools
# License: MIT

import sys
from remover.background import background
from remover.watermark import watermark

def remover():
    if len(sys.argv) < 3:
        print("Usage: remove <command>")
        sys.exit(1)
    if sys.argv[2] == "background" or sys.argv[2] == "bg":
        return background()
    if sys.argv[2] == "watermark" or sys.argv[2] == "wm":
        return watermark()
    
    else:
        print("No command found.\nCommand :\n\tbackground / bg\n\twatermark / wm")
        sys.exit(1)