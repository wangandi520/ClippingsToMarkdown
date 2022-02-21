# -*- coding: UTF-8 -*-
import sys
import os
import re
from pathlib import Path

# Highlights format support in 20220221
# support kindle , boox local and boox cloud
# Programmed by Andy
# v0.1

def readfile(filename):
    #readfile
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    #remove blank lines
    for i in filereadlines:
        if i == '\n':
            filereadlines.remove(i)
    #remove '\n' in line end
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()
    return filereadlines

def writefile(filename,filereadlines):
    #write file
    newfile = open(filename.with_suffix('.md'), mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()

def convertFromLocalStorage(filename):
    #readfile
    filereadlines = readfile(filename)
  
    #bookname,author style
    outputfile = []
    #outputfile.append('# ' + filereadlines[0][18:-2] + '\n\n')
    #outputfile.append('**' + filereadlines[1] + '**\n\n---\n\n')

    # format eachline to markdown
    # chapter,time,content style
    
    # if show time or not
    showTime = 0
    # if show annotations or not
    showAnnotations = 0
    # if show page num
    showPageNum = 0
    
    count = 0
    for each in filereadlines:
        if each.startswith('Reading Notes*|*'):
            outputfile.append('# ' + each[18:-2] + '\n\n')
            if(filereadlines[count + 1] != "null"):
                outputfile.append('**' + filereadlines[count + 1] + '**\n\n')
        elif each.startswith('Time：') and showTime:
            outputfile.append(each[5:] + '\n\n')
        elif each.startswith('【Original Text】'):
            outputfile.append('> ' + each[15:] + '\n\n')
        elif each.startswith('【Annotations】') and showAnnotations and len(each) > 13:
            outputfile.append('*' + each[13:] + '*\n\n')
        elif each.startswith('【Page Number】') and showPageNum:
            outputfile.append('*Page ' + each[13:] + '*\n\n')
        elif each.startswith("'-------------------"):
            outputfile.append('\n\n')
        count = count + 1
        # else:
            # outputfile.append('> ' + newcontent[i][j] + '\n\n')
    #write file
    writefile(filename,outputfile)
            

def main(filename):
    #read file
    file = open(filename, mode='r', encoding='UTF-8')
    firstline = file.readline()

    if (type(filename).__name__ == 'str'):
        filename = Path(filename)
    #Judge highlights from cloud note:onenote and evernote (False) or boox local storage (True) or kindle My Clippings.txt
    if filename.name != 'My Clippings.txt':
        convertFromLocalStorage(filename)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        for filenames in pathlib.Path('./').rglob('*.txt'):
            main(filenames)
    elif len(sys.argv) >= 2:
        for i in range(1 , len(sys.argv)):
            main(sys.argv[i])
