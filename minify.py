#!/usr/bin/env python3
# Copyright (c) 2022, Lunnos
# https://github.com/LunnosMp4/Minify
# License: MIT

import sys, requests, json

# Minify .xml / .c files (Comments not supported)
def minify_oneline(input_file, output_file):
    with open(input_file, "r") as f:
        data = f.read()
    data = data.replace("\n", "")
    data = data.replace("\r", "")
    data = data.replace("\t", "")
    data = data.replace("    ", "")
    data = data.replace("  ", "")
    with open(output_file, "w") as f:
        f.write(data)
    print("Minified to One line file: " + output_file)

# Minify .json files
def minify_json(input_file, output_file):
    with open(input_file, "r") as f:
        data = json.load(f)
    result = json.dumps(data, separators=(',', ':'))
    with open(output_file, "w") as f:
        f.write(result)
    print("Minified JSON file: " + output_file)

# Minify .html files
def minify_html(input_file, output_file):
    with open(input_file, "r") as f:
        data = f.read()
    result = requests.post('https://www.toptal.com/developers/html-minifier/api/raw', data=dict(input=data)).text
    with open(output_file, "w") as f:
        f.write(result)
    print("Minified HTML file: " + output_file)    

# Minify .css files
def minify_css(input_file, output_file):
    with open(input_file, "r") as f:
        data = f.read()
    result = requests.post('https://www.toptal.com/developers/cssminifier/api/raw', data=dict(input=data)).text
    with open(output_file, "w") as f:
        f.write(result)
    print("Minified CSS file: " + output_file)

# Minify .js files
def minify_js(input_file, output_file):
    with open(input_file, "r") as f:
        data = f.read()
    result = requests.post('https://www.toptal.com/developers/javascript-minifier/api/raw', data=dict(input=data)).text
    with open(output_file, "w") as f:
        f.write(result)
    print("Minified JS file: " + output_file)


def check_output(input_file):
    if (len(sys.argv) == 3):
        return sys.argv[2]
    if input_file.endswith(".css"):
        return input_file.replace(".css", ".min.css")
    if input_file.endswith(".js"):
        return input_file.replace(".js", ".min.js")
    if input_file.endswith(".html"):
        return input_file.replace(".html", ".min.html")
    if input_file.endswith(".json"):
        return input_file.replace(".json", ".min.json")
    if input_file.endswith(".xml"):
        return input_file.replace(".xml", ".min.xml")
    if input_file.endswith(".c"):
        return input_file.replace(".c", ".min.c")
    
def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: minify.h <input> <output>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = check_output(input_file)

    if input_file.endswith(".css"):
        minify_css(input_file, output_file)
        return
    if input_file.endswith(".js"):
        minify_js(input_file, output_file)
        return
    if input_file.endswith(".html"):
        minify_html(input_file, output_file)
        return
    if input_file.endswith(".json"):
        minify_json(input_file, output_file)
        return
    if input_file.endswith(".xml") or input_file.endswith(".c"):
        minify_oneline(input_file, output_file)
        return
    else:
        print("Unsupported file type")
        sys.exit(1)

if __name__ == '__main__':
    main()
