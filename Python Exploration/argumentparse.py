import argparse
import pyperclip
from PIL import Image
import pytesseract


def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text


parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--a")
parser.add_argument("--log")
parser.add_argument("-s", nargs=2)

args = parser.parse_args()


if args.log:
    fileName = args.log
    print(ocr_core(fileName))

elif args.s:
    inputFile = args.s[0]
    fileName = args.s[1]

    tempText = ocr_core(inputFile)
    f = open(fileName, "w+")

    for line in tempText:
        f.write(line)

    f.close()
