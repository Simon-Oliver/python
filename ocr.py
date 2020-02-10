from PIL import Image
import pytesseract
import time


def ocr_core(filename):
    tic = time.perf_counter()
    text = pytesseract.image_to_string(Image.open(filename))
    toc = time.perf_counter()
    print(f"{toc - tic:0.4f} seconds")
    return text


print(ocr_core('example.gif'))