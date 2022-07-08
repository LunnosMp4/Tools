#!/usr/bin/env python3
# Copyright (c) 2022, Lunnos
# https://github.com/LunnosMp4/Minify
# License: MIT

import sys, requests

def minify_css(input_file, output_file):
    with open(input_file, "r") as f:
        data = f.read()
    response = requests.post('https://www.toptal.com/developers/cssminifier/api/raw', data=dict(input=data)).text
    with open(output_file, "w") as f:
        f.write(response)
    print("Minified CSS file: " + output_file)

def minify_js(input_file, output_file):
    with open(input_file, "r") as f:
        data = f.read()
    response = requests.post('https://www.toptal.com/developers/javascript-minifier/api/raw', data=dict(input=data)).text
    with open(output_file, "w") as f:
        f.write(response)
    print("Minified JS file: " + output_file)
    

def check_output(input_file):
    if (len(sys.argv) == 3):
        return sys.argv[2]
    if input_file.endswith(".css"):
        return input_file.replace(".css", ".min.css")
    if input_file.endswith(".js"):
        return input_file.replace(".js", ".min.js")
    
def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: minify.py <input> <output>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = check_output(input_file)

    if input_file.endswith(".css"):
        minify_css(input_file, output_file)
        return
    if input_file.endswith(".js"):
        minify_js(input_file, output_file)
        return
    else:
        print("Unsupported file type")
        sys.exit(1)

if __name__ == '__main__':
    main()
