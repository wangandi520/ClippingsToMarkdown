# -*- coding: UTF-8 -*-
import sys

def formatfile(filename):
    #readfile
    file = open(filename, mode='r', encoding='UTF-8')
    filereadlines = file.readlines()
    file.close()
    #remove blank lines
    for i in filereadlines:
        if i == '\n':
            filereadlines.remove(i)
            
    #remove '\n' in line end
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()

    return filereadlines

def converterFromLocalStorage(filename):
    filereadlines = formatfile(filename)

    #remove '-------------------'
    for i in filereadlines:
        if '-------------------' in i:
            filereadlines.remove(i)
            
    #bookname,author style
    filereadlines[0] = '# ' + filereadlines[0][13:-2]
    filereadlines[1] = '**' + filereadlines[1] + '**'

    #chapter,time,sentence style
    for i in range(2 , (len(filereadlines)) - 3 , 4):
        filereadlines[i] = '## ' + filereadlines[i]
        filereadlines[i + 1] = '*' + filereadlines[i + 1][3:] + '*'
        filereadlines[i + 2] =  '> [原文]' + filereadlines[i + 2][4:]
        filereadlines[i + 3] = '*[批注]' + filereadlines[i + 3][4:] + '*'

    #add blank lines
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i] + '\n\n'

    #write file
    newfile = open(filename + '.md', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
            
def converterFromCloud(filename):
    filereadlines = formatfile(filename)
    
    #bookname,author style
    filereadlines[0] = '# ' + filereadlines[0]
    filereadlines[1] = '**' + filereadlines[1] + '**'

    #chapter,time,sentence style
    for i in range(2 , (len(filereadlines) - 3) , 3):
        filereadlines[i] = '## ' + filereadlines[i]
        filereadlines[i + 1] = '*' + filereadlines[i + 1] + '*'
        filereadlines[i + 2] =  '> ' + filereadlines[i + 2]
    filereadlines[len(filereadlines) - 1] = '**' + filereadlines[len(filereadlines) - 1][1:] + '**'
    
    #add blank lines
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i] + '\n\n'

    #write file
    newfile = open(filename + '.md', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()

def main(filename):
    #read file
    file = open(filename, mode='r', encoding='UTF-8')
    firstline = file.readline()

    #Judge highlights from cloud note:onenote and evernote (False) or boox local storage (True)
    fromLocalStorage = 'BOOX读书笔记' in firstline
    if fromLocalStorage:
        converterFromLocalStorage(filename)
    else:
        converterFromCloud(filename)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        filename = 'source.txt'
    else:
        filename = sys.argv[1]
    main(filename)