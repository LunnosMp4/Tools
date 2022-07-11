#!/usr/bin/env python3
# Copyright (c) 2022, Lunnos
# https://github.com/LunnosMp4/Tools
# License: MIT

from minify.minify import minify

def cmd():
    commands = {
        "min" : minify,
        "minify" : minify
    }
    return commands