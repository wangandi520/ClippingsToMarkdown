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
    outputfile.append('**' + filereadlines[1] + '**\n\n---')
    #converter each highlight block to [][]
    newcontent = []
    for i in range(len(linenum) - 1):
        eachcontent = []
        for j in range(linenum[i] + 1, linenum[i + 1]):
            if filereadlines[j] != '':
                eachcontent.append(filereadlines[j])
        newcontent.append(eachcontent)
    #format eachline to markdown
    #chapter,time,content style
    # Boox OS 3.1 new line for page number
    for i in range(len(newcontent)):
        if not newcontent[i][0].startswith('时间：'):
            lastChapterName = newcontent[i][0]
            print(lastChapterName)
        if newcontent[i][0].startswith('时间：'):
            #print(newcontent[i][0])
            outputfile.append('\n\n**' + lastChapterName + '**\n\n')
            outputfile.append('*' + newcontent[i][0][3:] + '*\n\n')
            outputfile.append('[原文]\n\n> ' + newcontent[i][1][4:])
            if newcontent[i][2][4:]:
                outputfile.append('\n\n[评论]\n\n> ' + newcontent[i][2][4:])
        #for j in range(3, len(newcontent[i]) - 1):
            #outputfile[-1] = outputfile[-1] + newcontent[i][j] + '\n\n'
            outputfile[-1] = outputfile[-1].rstrip() + '\n\n'
            outputfile.append('[页码]' + newcontent[i][(len(newcontent[i]) - 1)][4:] + '\n\n')
            outputfile.append('---')
        else:
            #print(newcontent[i][0])
            outputfile.append('\n\n**' + newcontent[i][0] + '**\n\n')
            outputfile.append('*' + newcontent[i][1][3:] + '*\n\n')
            outputfile.append('[原文]\n\n> ' + newcontent[i][2][4:])
            if newcontent[i][3][4:]:
                outputfile.append('\n\n[评论]\n\n> ' + newcontent[i][3][4:])
        #for j in range(3, len(newcontent[i]) - 1):
            #outputfile[-1] = outputfile[-1] + newcontent[i][j] + '\n\n'
            outputfile[-1] = outputfile[-1].rstrip() + '\n\n'
            outputfile.append('[页码]' + newcontent[i][(len(newcontent[i]) - 1)][4:] + '\n\n')
            outputfile.append('---')
            
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
