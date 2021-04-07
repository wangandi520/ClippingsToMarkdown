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


def convertFromCloud(filename):
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
    section = []
    #split into sectionitem
    for i in range(0,len(indexnum) - 1):
        sectionitem = []
        for j in range(indexnum[i] - 1,indexnum[i + 1] - 1):
            if not filereadlines[indexnum[i] - 1].startswith('注 |') and filereadlines[indexnum[i] + 1] != filereadlines[indexnum[i] - 1]:
                sectionitem.append(filereadlines[j])
        section.append(sectionitem)
    print(section[1])
    for i in section:
        outputfile.append('**' + i[0] + '**\n\n')
        outputfile.append('*' + i[1] + '*\n\n')
        j = 2
        while j < len(i): 
            if i[j].startswith('注 |'):
                outputfile.append('[评论] ' + i[j][4:] + '\n\n')
            else:
                outputfile.append('> ' + i[j] + '\n\n')
            j = j + 1
        outputfile.append('---\n\n')
    outputfile.append('*' + filereadlines[-1] + '*\n')
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
        convertFromCloud(filename)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        for filenames in pathlib.Path('./').rglob('*.txt'):
            main(filenames)
    elif len(sys.argv) >= 2:
        for i in range(1 , len(sys.argv)):
            main(sys.argv[i])
