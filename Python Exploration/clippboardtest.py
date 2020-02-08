import pyperclip

prev = ""

while True:
    tempTxt = pyperclip.paste()
    if(tempTxt != prev):
        prev = tempTxt
        print(tempTxt)

