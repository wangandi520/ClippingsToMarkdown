# -*- coding: UTF-8 -*-
import sys
import os
from pathlib import Path

# Highlights format support in 20220222
# support kindle , boox local and boox cloud
# Programmed by Andy
# v0.2

def readfile(filename):
    # readfile
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    # show open file location
    print('Open: ' + str(filename))
    # remove blank lines
    for i in filereadlines:
        if i == '\n':
            filereadlines.remove(i)
    # remove '\n' in line end
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()
    return filereadlines

def writefile(filename,filereadlines):
    # write file
    # file name
    newfile = open(filename.with_suffix('.md'), mode='w', encoding='UTF-8')
    # show file location
    print('Save: ' + str(filename.with_suffix('.md')))
    newfile.writelines(filereadlines)
    newfile.close()

def convertFromLocalStorage(filename):
    #readfile
    filereadlines = readfile(filename)
    outputfile = []
    
    # show time = 1 or not = 0
    showTime = 1
    # show annotations = 1 or not = 0
    showAnnotations = 1
    # show page num = 1 or not = 0
    showPageNum = 1
    # show author = 1 or not = 0
    showAuthor = 1
    
    count = 0
    for each in filereadlines:
        if each.startswith('Reading Notes'):
            # bookname:
            outputfile.append('# ' + each[18:-2] + '\n\n')
            startIndex = each.find('<') + 2
            outputfile.append('Book: ' + each[startIndex:-2] + '\n')
            if(filereadlines[count + 1] != "null" and showAuthor):
                # author
                outputfile.append('Author: ' + filereadlines[count + 1] + '\n\n')
            else:
                outputfile.append('\n')
        elif each.startswith('Time：') and showTime:
            # time
            outputfile.append(each[5:] + '\n\n')
        elif each.startswith('【Original Text】'):
            # paragraph
            outputfile.append(each[15:] + '\n\n')
        elif each.startswith('【Annotations】') and showAnnotations and len(each) > 13:
            # annotations
            outputfile.append('*' + each[13:] + '*\n\n')
        elif each.startswith('【Page Number】') and showPageNum:
            # page number
            outputfile.append('*Page ' + each[13:] + '*\n\n')
        elif each.startswith("'-------------------"):
            outputfile.append('\n\n')
        count = count + 1
    # write file
    writefile(filename,outputfile)
            

def main(filename):
    # read file
    file = open(filename, mode='r', encoding='UTF-8')
    firstline = file.readline()

    if (type(filename).__name__ == 'str'):
        filename = Path(filename)
    convertFromLocalStorage(filename)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        # origin file type: txt
        for filenames in pathlib.Path('./').rglob('*.txt'):
            main(filenames)
    elif len(sys.argv) >= 2:
        for i in range(1 , len(sys.argv)):
            main(sys.argv[i])
