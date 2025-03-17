# -*- coding: UTF-8 -*-
import sys
import os
import pathlib
import re

# Highlights format support in 20210407
# support kindle , boox local and boox cloud
# Programmed by Andy
# v0.4

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
    #get '-------------------' line number
    linenum = [1]
    for i in range(len(filereadlines)):
        if '-------------------' in filereadlines[i]:
            linenum.append(i)
    #bookname,author style
    outputfile = []
    outputfile.append('# ' + filereadlines[0][13:-2] + '\n\n')
    outputfile.append('**' + filereadlines[1] + '**\n\n---\n\n')
    #converter each highlight block to [][]
    newcontent = []
    for i in range(len(linenum) - 1):
        eachcontent = []
        for j in range(linenum[i] + 1, linenum[i + 1]):
            if filereadlines[j] != '':
                eachcontent.append(filereadlines[j])
        newcontent.append(eachcontent)
    # format eachline to markdown
    # chapter,time,content style
    # Boox OS 3.1 new line for page number
    for i in range(len(newcontent)):
        start = 0
        if newcontent[i][0].startswith('时间：'):
            start = 0
        else:
            outputfile.append('**' + newcontent[i][0] + '**\n\n')
            start = 1
        outputfile.append('*' + newcontent[i][start][3:] + '*\n\n')
        outputfile.append('[原文]\n\n')
        start = start + 1
        for j in range(start, len(newcontent[i])):
            if newcontent[i][j].startswith('【原文】'):
                outputfile.append('> ' + newcontent[i][j][4:] + '\n\n')
            elif newcontent[i][j].startswith('【批注】'):
                outputfile.append('[批注]\n\n> ' + newcontent[i][j][4:] + '\n\n')
            elif newcontent[i][j].startswith('【页码】'):
                outputfile.append('[页码]' + newcontent[i][j][4:] + '\n\n')
            else:
                outputfile.append('> ' + newcontent[i][j] + '\n\n')
        outputfile.append('---\n\n')    
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
