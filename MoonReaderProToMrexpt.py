# encoding:utf-8
# https://github.com/wangandi520/ClippingsToMarkdown
# tested Moon Reader Pro 8.2
# Programmed by Andy
# v0.6

from pathlib import Path
import sys
import time

def readfile(filename):
    # 读取文件
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()
    return filereadlines

def writefile(filename,filereadlines):
    # 写入.md文件
    newfile = open(Path(filename).parent.joinpath(Path(filename).stem + '.md'), mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    print('完成：' + str(Path(filename).name))
    
def convertMoonReadermrexpt(filename):
    # 读取.mrexpt文件
    filereadlines = readfile(filename)
    print('处理：' + str(Path(filename).name))
    # 书名作者
    eachcontent = []
    eachcontent.append('# ' + filereadlines[5])
    eachcontent.append('\n---')
    # 标注计数
    clippingsCount = 0
    # 标注
    for i in range(4, len(filereadlines), 17):
        eachcontent.append('\n\n> ' + filereadlines[i+12] + '\n\n')
        if filereadlines[i+11] != '':
            eachcontent.append('**' + filereadlines[i+11] + '**\n\n')
        # 时间格式转换
        clippingTime = float(filereadlines[i+9])/1000
        clippingTimeTransfered = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(clippingTime))
        eachcontent.append('*' + clippingTimeTransfered + '*\n\n')
        eachcontent.append('---')
        clippingsCount = clippingsCount + 1
    eachcontent.append('\n')
    clippingsCount = '\n\n**共' + str(clippingsCount) + '条标注**\n'
    # 如果不需要标注计数，请把下一行前加#
    eachcontent.insert(1, clippingsCount)
    # 写入
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