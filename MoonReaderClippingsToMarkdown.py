# -*- coding: UTF-8 -*-
import sys
import os
import pathlib
import time

# Highlights format support in 20200313
# support kindle , boox local and boox cloud
# Programmed by Andy
# v0.3

def readfile(filename):
    #readfile
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    #remove blank lines
    #for i in filereadlines:
        #if i == '\n':
            #filereadlines.remove(i)
    #remove '\n' in line end
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()
    return filereadlines

def writefile(filename,filereadlines):
    #write file
    newfile = open(filename.with_suffix('.md'), mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    
def converterFromMoonReadermrexpt(filename):
    #readfile
    filereadlines = readfile(filename)
    #bookname,author style
    eachcontent = []
    #eachcontent.append(str(len(filereadlines)))
    eachcontent.append('# ' + filereadlines[5] + '\n\n')
    for i in range(16, len(filereadlines), 17):
        eachcontent.append(filereadlines[i] + '\n\n')
        #time
        clippingTime = float(float(filereadlines[i+14])/1000) 
        clippingTimeTransfered = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(clippingTime))
        eachcontent.append(str(clippingTimeTransfered))
    #write file
    writefile(filename,eachcontent)
    
def main(filename):
    #read file
    file = open(filename, mode='r', encoding='UTF-8')
    firstline = file.readline()

    if (type(filename).__name__ == 'str'):
        filename = Path(filename)
    #Judge highlights from cloud note:onenote and evernote (False) or boox local storage (True) or kindle My Clippings.txt
    converterFromMoonReadermrexpt(filename)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        for filenames in pathlib.Path('./').rglob('*.mrexpt'):
            main(filenames)
    elif len(sys.argv) >= 2:
        for i in range(1 , len(sys.argv)):
            main(sys.argv[i])