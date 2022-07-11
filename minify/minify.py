#!/usr/bin/env python3
# Copyright (c) 2022, Lunnos
# https://github.com/LunnosMp4/Tools
# License: MIT

import sys, requests, json

def minify_sql(input_file, output_file):
    with open(input_file, "r") as f:
        data = f.read()
    data = data.replace("\n", " ")
    data = data.replace("    ", "")
    data = data.replace("  ", "")
    with open(output_file, "w") as f:
        f.write(data)
    print("Minified SQL file: " + output_file)

# Minify .xml (Comments not supported)
def minify_xml(input_file, output_file):
    with open(input_file, "r") as f:
        data = f.read()
    data = data.replace("\n", "")
    data = data.replace("\r", "")
    data = data.replace("\t", "")
    data = data.replace("    ", "")
    data = data.replace("  ", "")
    with open(output_file, "w") as f:
        f.write(data)
    print("Minified XML file: " + output_file)

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
    if (len(sys.argv) == 4):
        return sys.argv[3]
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
    if input_file.endswith(".sql"):
        return input_file.replace(".sql", ".min.sql")
    
def minify():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: minify <input> <output>")
        sys.exit(1)

    input_file = sys.argv[2]
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
    if input_file.endswith(".xml"):
        minify_xml(input_file, output_file)
        return
    if input_file.endswith(".sql"):
        minify_sql(input_file, output_file)
        return
    else:
        print("Unsupported file type")
        sys.exit(1)
