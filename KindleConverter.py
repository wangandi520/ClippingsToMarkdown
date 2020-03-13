# -*- coding: UTF-8 -*-
import sys

from pathlib import Path

#Highlights format support in 20200313
#Programmed by Andy
def readfile(filename):
    #readfile
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    #remove blank lines
    for i in filereadlines:
        if i == '\n':
            filereadlines.remove(i)
    #remove '\n' in line end and middle
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()
    return filereadlines

def writefile(filename,filereadlines):
    #write file
    newfile = open('My Clippings.md', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()

def converter(filename):
    #readfile
    filereadlines = readfile(filename)
    #get '-------------------' line number
    linenum = [-1]
    for i in range(len(filereadlines)):
        if '==========' in filereadlines[i]:
            linenum.append(i)
    outputfile = []
    #converter each highlight block to [][]
    newcontent = []
    for i in range(len(linenum) - 1):
        eachcontent = []
        for j in range(linenum[i] + 1, linenum[i + 1]):
            if filereadlines[j] != '':
                eachcontent.append(filereadlines[j])
        newcontent.append(eachcontent)
    #format eachline to markdown
    #chapter,time,sentence style
    for i in range(len(newcontent)):
        outputfile.append('**' + newcontent[i][0] + '**\n\n')
        outputfile.append('*' + newcontent[i][1] + '*\n\n')
        if len(newcontent[i]) >= 3:
            outputfile.append('> ' + newcontent[i][2] + '\n\n')
        outputfile.append('---\n\n')
    #write file
    writefile(filename,outputfile)

def main(filename):
    #read file
    converter(filename)

if __name__ == '__main__':
    kindleclippingsfilename = 'My Clippings.txt'
    main(kindleclippingsfilename)