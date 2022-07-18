#!/usr/bin/env python3
# Copyright (c) 2022, Lunnos
# https://github.com/LunnosMp4/Tools
# License: MIT

from pydub import AudioSegment
import os, sys

def audio(input_file, ext):
    if not os.path.isfile(input_file):
        print("Input file is not a file or doesn't exist.")
        sys.exit(1)

    input_format = os.path.splitext(input_file)[1][1:]
    output_file = os.path.splitext(input_file)[0] + "_converted." + ext

    input_audio = AudioSegment.from_file(input_file, format=input_format)
    input_audio.export(output_file, format=ext)
    print("Converting " + input_file + " to " + output_file)
