#!/usr/bin/env python3
# Copyright (c) 2022, Lunnos
# https://github.com/LunnosMp4/Tools
# License: MIT

from collections import OrderedDict
import io, shutil, os, sys

import img2pdf
from PIL import Image
from PyPDF2 import PdfFileReader


def is_gray(a, b, c):
    r = 40
    if a + b + c < 350:
        return True
    if abs(a - b) > r:
        return False
    if abs(a - c) > r:
        return False
    if abs(b - c) > r:
        return False
    return True

def remove_watermark(image):
    image = image.convert("RGB")
    color_data = image.getdata()

    img = 0
    new_color = []
    for item in color_data:
        if is_gray(item[0], item[1], item[2]):
            new_color.append(item)
        else:
            new_color.append((255, 255, 255))

    image.putdata(new_color)
    return image

def process_page(pdf, page_index):
    content = pdf.getPage(page_index)['/Resources']['/XObject'].getObject()
    images = {}
    for obj in content:
        if content[obj]['/Subtype'] == '/Image':
            size = (content[obj]['/Width'], content[obj]['/Height'])
            data = content[obj]._data
            if content[obj]['/ColorSpace'] == '/DeviceRGB':
                mode = "RGB"
            else:
                mode = "P"

            if content[obj]['/Filter'] == '/FlateDecode':
                img = Image.frombytes(mode, size, data)
            else:
                img = Image.open(io.BytesIO(data))
            images[int(obj[3:])] = img
    images = OrderedDict(sorted(images.items())).values()
    widths, heights = zip(*(i.size for i in images))
    total_height = sum(heights)
    max_width = max(widths)
    concat_image = Image.new('RGB', (max_width, total_height))
    offset = 0
    for i in images:
        concat_image.paste(i, (0, offset))
        offset += i.size[1]
    concat_image = remove_watermark(concat_image)
    concat_image.save("./temp/{}.jpg".format(page_index))

def watermark():
    if len(sys.argv) < 4:
        print("Usage: remove wm <file.pdf>")
        sys.exit(1)

    directory = './temp/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    input_path = sys.argv[3]
    output_path = os.path.splitext(input_path)[0] + "_2.pdf"

    images_path = []
    pdf = PdfFileReader(open(input_path, "rb"))
    for i in range(0, pdf.getNumPages()):
        print("Processing page {}/{}".format(i + 1, pdf.getNumPages()))
        images_path.append("./temp/{}.jpg".format(i))
        process_page(pdf, i)

    output_path.write(img2pdf.convert(*list(map(img2pdf.input_images, images_path))))

    shutil.rmtree(directory, True)
