# -*- coding: UTF-8 -*-
import sys
import os
from pathlib import Path

# Highlights format support in 20220307
# support kindle , boox local and boox cloud
# Programmed by Andy
# v0.1

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
   
    title = filereadlines[0] .split(' - ')
    # book name
    outputfile.append('# ' + title[0] + '\n\n')
    startIndex = title[1].rfind('(')
    # author
    outputfile.append('*' + title[1][0: startIndex - 1]+ '*\n\n')
    # highlight and note count
    outputfile.append('*' + title[1][startIndex:]+ '*\n\n')
    
    for each in filereadlines[1:]:
        if (each[0] == '◆'):
            # section
            outputfile.append('## ' + each[2:] + '\n\n')
        elif (each[0] == '▪'):
            # paragraph
            outputfile.append('> ' + each[2:] + '\n\n')
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
