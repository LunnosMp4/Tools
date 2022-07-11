#!/usr/bin/env python3
# Copyright (c) 2022, Lunnos
# https://github.com/LunnosMp4/Tools
# License: MIT

import sys, os, jsbeautifier

def unminify_js(input_file, output_file):
    data = jsbeautifier.beautify_file(input_file)

    with open(output_file, "w") as f:
        f.write(data)
    print("Unminified file: " + output_file)

def check_output(input_file):
    if (len(sys.argv) == 4):
        if not os.path.isfile(sys.argv[3]):
            print("Output file not found.")
            sys.exit(1)
        return sys.argv[3]
    if input_file.endswith(".css") or input_file.endswith(".min.css"):
        return os.path.splitext(input_file)[0] + "_unminify.css"
    if input_file.endswith(".js") or input_file.endswith(".min.js"):
        return os.path.splitext(input_file)[0] + "_unminify.js"
    if input_file.endswith(".html"):
        return os.path.splitext(input_file)[0] + "_unminify.html"
    if input_file.endswith(".json"):
        return os.path.splitext(input_file)[0] + "_unminify.json"
    if input_file.endswith(".xml"):
        return os.path.splitext(input_file)[0] + "_unminify.xml"
    if input_file.endswith(".sql"):
        return os.path.splitext(input_file)[0] + "_unminify.sql"

def unminify():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: minify <input> <output>")
        sys.exit(1)
    
    input_file = sys.argv[2]
    if not os.path.isfile(input_file):
        print("Input file not found.")
        sys.exit(1)

    output_file = check_output(input_file)

    if input_file.endswith(".js"):
        unminify_js(input_file, output_file)
        return
    else:
        print("Unminify is only supported for JS files at the moment.")
        sys.exit(1)

    