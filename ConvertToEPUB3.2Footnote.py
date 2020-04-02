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

def writefile(filereadlines):
    #write file
    with open('footnote1.txt', mode='w', encoding='UTF-8') as newfile:
        newfile.writelines(filereadlines)

def converter():
    #readfile
    filereadlines = readfile('footnote.txt')
    #get '-------------------' line number
    newlines = []
    newlines.append('  <section epub:type="footnotes">\n')
    num = 1
    for i in filereadlines:
        if num < 10:
            newlines.append('  <aside epub:type="footnote" id="footnote0'  + str(num) + '"><p>[' + str(num) + ']' + i[45:-4] + '</p></aside>\n')
        else:
            newlines.append('  <aside epub:type="footnote" id="footnote'  + str(num) + '"><p>[' + str(num) + ']'+ i[46:-4] + '</p></aside>\n')
        #print(i[45:-4])
        num = num + 1
    newlines.append('  </section>\n')
    writefile(newlines)

if __name__ == '__main__':
    converter()