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

def converterFromLocalStorage(filename):
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
    for i in range(len(newcontent)):
        outputfile.append('\n\n**' + newcontent[i][0] + '**\n\n')
        outputfile.append('*' + newcontent[i][1][3:] + '*\n\n')
        outputfile.append('[原文]\n\n> ' + newcontent[i][2][4:])
        for j in range(3, len(newcontent[i]) - 1):
            outputfile[-1] = outputfile[-1] + newcontent[i][j] + '\n\n'
        outputfile[-1] = outputfile[-1].rstrip() + '\n\n'
        outputfile.append('*[批注]' + newcontent[i][(len(newcontent[i]) - 1)][4:] + '*\n\n')
        outputfile.append('---')
    #write file
    writefile(filename,outputfile)
            
def converterFromCloud(filename):
    #readfile
    filereadlines = readfile(filename)
    #output
    outputfile = []
    #title
    outputfile.append('# ' + filereadlines[0] + '\n\n')
    #author
    outputfile.append('**' + filereadlines[1] + '**\n\n---\n\n')
    #check time format
    timereg = r'(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2})'
    indexnum = []
    #get time line number in file
    for i in range(0,len(filereadlines)):  
        if re.match(timereg,filereadlines[i]):
            indexnum.append(i)
        elif filereadlines[i].startswith('BOOX读书笔记来自'):
            indexnum.append(i + 1)
    
    #print(indexnum)
    section = []
    #split into sectionitem
    for i in range(0,len(indexnum) - 1):
        sectionitem = []
        for j in range(indexnum[i] - 1,indexnum[i + 1] - 1):
            sectionitem.append(filereadlines[j])
        section.append(sectionitem)
    for i in section:
        outputfile.append('**' + i[0] + '**\n\n')
        outputfile.append('*' + i[1] + '*\n\n')
        j = 2
        while j < len(i): 
            outputfile.append('> ' + i[j] + '\n\n')
            j = j + 1
        outputfile.append('---\n\n')


    
    outputfile.append('*' + filereadlines[-1] + '*\n')
    print(outputfile)
    #write file
    writefile(filename,outputfile)

def main(filename):
    #read file
    file = open(filename, mode='r', encoding='UTF-8')
    firstline = file.readline()

    if (type(filename).__name__ == 'str'):
        filename = Path(filename)
    #Judge highlights from cloud note:onenote and evernote (False) or boox local storage (True) or kindle My Clippings.txt
    if 'BOOX读书笔记' in firstline and filename.name != 'My Clippings.txt':
        converterFromLocalStorage(filename)
    elif filename.name != 'My Clippings.txt':
        converterFromCloud(filename)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        for filenames in pathlib.Path('./').rglob('*.txt'):
            main(filenames)
    elif len(sys.argv) >= 2:
        for i in range(1 , len(sys.argv)):
            main(sys.argv[i])
