# encoding:utf-8
# Highlights format support in 20220912
# tested Moon Reader Pro 7.6
# Programmed by Andy
# v0.5

from pathlib import Path
import sys
import time

def readfile(filename):
    # readfile
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()
    return filereadlines

def writefile(filename,filereadlines):
    # write file
    newfile = open(Path(filename).parent.joinpath(Path(filename).stem + '.md'), mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    
def convertMoonReadermrexpt(filename):
    # readfile
    filereadlines = readfile(filename)
    # bookname,author style
    eachcontent = []
    eachcontent.append('# ' + filereadlines[5])
    eachcontent.append('\n\n---')
    for i in range(4, len(filereadlines), 17):
        eachcontent.append('\n\n> ' + filereadlines[i+12] + '\n\n')
        # time
        clippingTime = float(filereadlines[i+9])/1000
        clippingTimeTransfered = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(clippingTime))
        eachcontent.append('*' + clippingTimeTransfered + '*\n\n')
        eachcontent.append('---')
    eachcontent.append('\n')
    # write file
    writefile(filename,eachcontent)
    
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('*.mrexpt'):
                convertMoonReadermrexpt(file)
        if Path.is_file(Path(aPath)):
            if (Path(aPath).suffix == '.mrexpt'):
                convertMoonReadermrexpt(aPath)
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass