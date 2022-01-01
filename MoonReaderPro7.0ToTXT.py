# encoding:utf-8
# Highlights format support in 20210928
# tested Moon Reader Pro 6.9
# Programmed by Andy
# v0.4

from pathlib import Path
import sys
import time

def readfile(filename):
    # readfile
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    return filereadlines

def writefile(filename,filereadlines):
    # write file
    newfile = open(Path(filename).stem + '.md', mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    
def convertMoonReaderTXT(filename):
    # readfile
    filereadlines = readfile(filename)
    # bookname,author style
    eachcontent = []
    bookName = filereadlines[0].split(' - ')[0]
    findLoc = filereadlines[0].split(' - ')[1].find('(')
    authorName = filereadlines[0].split(' - ')[1][0:findLoc - 1]
    otherMsg = filereadlines[0].split(' - ')[1][findLoc:].replace('\n','')
    eachcontent.append('---\n\n# ' + bookName + '\n\n')
    eachcontent.append('**' + authorName + '**\n\n')
    eachcontent.append('**' + otherMsg + '**\n\n')
    for i in filereadlines[3:]:
        if (i[0] == '◆'):
            eachcontent.append('---\n\n## ' + i[2:] + '\n')
        # time
        elif (i[0] != '\n'):
            eachcontent.append('> ' + i[1:] + '\n')
    
    eachcontent.append('---')
    # write file
    writefile(filename,eachcontent)
    
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*.txt'):
                convertMoonReaderTXT(file)
        if Path.is_file(Path(aPath)):
            if (Path(aPath).suffix == '.txt'):
                convertMoonReaderTXT(aPath)
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass