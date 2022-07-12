#!/usr/bin/env python3
# Copyright (c) 2022, Lunnos
# https://github.com/LunnosMp4/Tools
# License: MIT

from cmd import cmd
import sys

def main():
    commands = cmd()
    if len(sys.argv) > 1:
        if sys.argv[1] in commands:
            commands[sys.argv[1]]()
        else:
            print("Command not found.")
    else:
        print("No command specified.")

if __name__ == "__main__":
    main()