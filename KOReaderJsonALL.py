# encoding:utf-8
# Highlights format support in 20210904
# tested koreader android 2021.09
# Programmed by Andy
# v0.4

from pathlib import Path
import sys
import os
import json
import time
import datetime

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
    newfile = open(Path(filename).stem + '.md', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
            
def converterFromKOReaderJson(filename):
    # read json file
    allBooks = readfile(filename)
    outputfile = []
    for eachBook in allBooks:
        jsonData = json.loads(eachBook)
        outputfile.append('# ' + jsonData['title'] + '\n\n---\n\n')
        for key in jsonData:
            try:
                outputfile.append('> ' + jsonData[key][0]['text'] + '\n\n')
                outputfile.append('*' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(jsonData[key][0]['time'])) + '*\n\n---\n\n')
            except TypeError:
                continue
            except KeyError:
                continue
    writefile(filename,outputfile)

def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*.json'):
                converterFromKOReaderJson(file)
        if Path.is_file(Path(aPath)):
            if (Path(aPath).suffix == '.json'):
                converterFromKOReaderJson(aPath)

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass
