# -*- coding: UTF-8 -*-
import sys
import os
import pathlib

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
    
def converterFromKindleSorted(filename):
    #readfile
    filereadlines = readfile(filename)
    #get '==========' line number
    linenum = [-1]
    for i in range(len(filereadlines)):
        if '==========' in filereadlines[i]:
            linenum.append(i)
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
    sortedcontent = {}
    for i in range(len(newcontent)):
        if newcontent[i][0] not in sortedcontent:
            if len(newcontent[i]) >= 3:
                sortedcontent[newcontent[i][0]]=[]
                sortedcontent[newcontent[i][0]].append([newcontent[i][1] , newcontent[i][2]])
        elif newcontent[i][0] in sortedcontent:
            if len(newcontent[i]) >= 3:
                sortedcontent[newcontent[i][0]].append([newcontent[i][1] , newcontent[i][2]])
    outputfile = ['[TOC]\n\n---\n\n']
    for key in sortedcontent:
        outputfile.append('## ' + key + '\n\n')
        for j in range(len(sortedcontent[key])):
            outputfile.append('*' + sortedcontent[key][j][0] + '*\n\n')
            outputfile.append('> ' + sortedcontent[key][j][1] + '\n\n')
        outputfile.append('---\n\n')
    outputfile[-1] = '---'
    #write file
    writefile(filename,outputfile)

def converterFromKindleNatured(filename):
    #readfile
    filereadlines = readfile(filename)
    #get '==========' line number
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
    #chapter,time,content style
    for i in range(len(newcontent)):
        outputfile.append('## ' + newcontent[i][0] + '\n\n')
        outputfile.append('*' + newcontent[i][1] + '*\n\n')
        if len(newcontent[i]) >= 3:
            outputfile.append('> ' + newcontent[i][2] + '\n\n')
        outputfile.append('---\n\n')
    outputfile[-1] = '---'
    #write file
    writefile(filename,outputfile)
    
def main(filename):
    #read file
    file = open(filename, mode='r', encoding='UTF-8')
    firstline = file.readline()

    if (type(filename).__name__ == 'str'):
        filename = Path(filename)
    #Judge highlights from cloud note:onenote and evernote (False) or boox local storage (True) or kindle My Clippings.txt
    if filename.name == 'My Clippings.txt' and os.path.basename(__file__) == 'KindleClippingsToMarkdown.py':
        converterFromKindleNatured(filename)
    elif filename.name == 'My Clippings.txt' and os.path.basename(__file__) == 'KindleClippingsToMarkdownSorted.py':
        converterFromKindleSorted(filename)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        for filenames in pathlib.Path('./').rglob('*.txt'):
            main(filenames)
    elif len(sys.argv) >= 2:
        for i in range(1 , len(sys.argv)):
            main(sys.argv[i])