# -*- coding=utf-8 -*-

from PIL import Image
import os
# import argparse
# import glob

# imagelist= sorted(glob.glob(r'C:\Users\Administrator\Desktop\py'))
path = "C:\\Users\\Administrator\\Desktop\\py\\img\\image"
outpath = "C:\\Users\\Administrator\\Desktop\\py\\img\\output"
filelist = os.listdir(path)
ascii_char = list("* ")

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char) 
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

for filename in filelist:
    img = Image.open(path + '\\' + filename)
    # print(img.format)
    # WIDTH = int(img.size[1] / 10)
    # HEIGHT = int(img.size[0] / 10)
    WIDTH = int(img.size[1] / 4)
    HEIGHT = int(img.size[0] / 4)
    OUTPUT = outpath + '\\' + filename + '.txt'

    img = img.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*img.getpixel((j,i)))
        txt += '\n'
    # print(txt)

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("filename.txt",'w') as f:
            f.write(txt)
    pass