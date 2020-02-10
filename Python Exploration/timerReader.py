import threading
import os

temp = 0

def printit():
    global temp
    threading.Timer(0.1, printit).start()
    if temp != os.stat("./files/test.txt").st_mtime:
        print('File Changed')
        temp = os.stat("./files/test.txt").st_mtime


printit()


