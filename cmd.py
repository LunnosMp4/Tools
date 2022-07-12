#!/usr/bin/env python3
# Copyright (c) 2022, Lunnos
# https://github.com/LunnosMp4/Tools
# License: MIT

from minify.minify import minify
from converter.convert import convert
from unminify.unminify import unminify
from remover.remover import remover

def cmd():
    commands = {
        "min" : minify,
        "minify" : minify,

        "unmin" : unminify,
        "unminify" : unminify,

        "cvt" : convert,
        "convert" : convert,

        "remove" : remover,
        "rm" : remover, 
    }
    return commands