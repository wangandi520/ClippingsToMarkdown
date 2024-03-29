# -*- coding: UTF-8 -*-
import sys
import os
import pathlib
import re

# Highlights format support in 20200313
# support kindle , boox local and boox cloud
# Programmed by Andy
# v0.3

def readfile(filename):
    # readfile
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
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
    newfile = open(filename.with_suffix('.md'), mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()

def converterFromClipboard(filename):
    # readfile
    filereadlines = readfile(filename)
    
    #book title,author style
    outputfile = []
    outputfile.append('# ' + filereadlines[0] + '\n\n')
    outputfile.append('**' + filereadlines[1] + '**\n\n')
    outputfile.append('*' + filereadlines[2] + '*\n\n---')
    #converter each highlight block to [][]
    for i in range(3, len(filereadlines)):
        if filereadlines[i].startswith('◆'):
            outputfile.append('---\n\n**' + filereadlines[i][2:] + '**\n\n')
        if filereadlines[i].startswith('>>'):
            outputfile.append('> ' + filereadlines[i][3:] + '\n\n')
        print(filereadlines[i])
    #write file
    writefile(filename,outputfile)
            


def main(filename):
    # read file
    file = open(filename, mode='r', encoding='UTF-8')
    firstline = file.readline()

    if (type(filename).__name__ == 'str'):
        filename = Path(filename)
    # Paste content from weread to *.txt
    converterFromClipboard(filename)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        for filenames in pathlib.Path('./').rglob('*.txt'):
            main(filenames)
    elif len(sys.argv) >= 2:
        for i in range(1 , len(sys.argv)):
            main(sys.argv[i])
