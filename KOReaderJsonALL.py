# -*- coding: UTF-8 -*-
import sys
import os
import pathlib
import json
import time
import datetime

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
    #write file
    newfile = open(filename.with_suffix('.md'), mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
            
def converterFromJson(filename):
    # read json file
    allBooks = readfile(filename)
    # how many books
    bookCount = len(allBooks)
    
    outputfile = []
    for echoBook in allBooks:
        jsonData = json.loads(echoBook)
        outputfile.append('# ' + jsonData['title'] + '\n\n')
        for key in jsonData:
            try:
                outputfile.append('> ' + jsonData[key][0]['text'] + '\n\n')
                outputfile.append('*' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(jsonData[key][0]['time'])) + '*\n\n')
            except TypeError:
                continue
            except KeyError:
                continue
        outputfile.append('---\n\n')
    writefile(filename,outputfile)

def main(filename):
    # read file
    file = open(filename, mode='r', encoding='UTF-8')
    firstline = file.readline()
    if (type(filename).__name__ == 'str'):
        filename = Path(filename)
    converterFromJson(filename)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        for filenames in pathlib.Path('./').rglob('*.json'):
            main(filenames)
    elif len(sys.argv) >= 2:
        for i in range(1 , len(sys.argv)):
            main(sys.argv[i])
