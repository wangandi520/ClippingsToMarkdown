# encoding:utf-8
# https://github.com/wangandi520/ClippingsToMarkdown
# tested Moon Reader Pro 8.6
# Programmed by Andy
# v0.1
# 转换出的markdown文件直接可以在hexo里使用

from pathlib import Path
import sys
import time

def readfile(filename):
    # 读取.mrexpt文件
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    for i in range(len(filereadlines)):
        filereadlines[i] = filereadlines[i].rstrip()
    return filereadlines

def writefile(filename,filereadlines):
    # 写入.md文件
    newfile = open(Path(filename).parent.joinpath(Path(filename).stem + '标注.md'), mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    print('完成：' + str(Path(filename).name))
    
def convertMoonReadermrexpt(filename):
    # 设置文章标签tags
    myTags = ['阅读', '标注', '读书笔记']
    # 设置文章分类categories
    myCategories = '读书笔记'
    # 设置hexo文章头部信息Front-matter
    myFrontMatter = '---\ntitle: ' + str(Path(filename).stem) + ' 标注\ntoc: true\ntags:\n- ' + '\n- '.join(myTags) + '\ncategories: \n- ' + myCategories + '\ndate: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n---\n\n'
    # 读取文件
    filereadlines = readfile(filename)
    print('处理：' + str(Path(filename).name))
    # 书名作者
    eachcontent = []
    eachcontent.append(myFrontMatter)
    eachcontent.append('# ' + Path(filereadlines[5]).stem)
    eachcontent.append('\n---')
    # 标注计数
    clippingsCount = 0
    for i in range(4, len(filereadlines), 17):
        eachcontent.append('\n\n> ' + filereadlines[i+12] + '\n\n')
        if filereadlines[i+11] != '':
            eachcontent.append('**' + filereadlines[i+11] + '**\n\n')
        # 时间转换
        clippingTime = float(filereadlines[i+9])/1000
        clippingTimeTransfered = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(clippingTime))
        eachcontent.append('*' + clippingTimeTransfered + '*\n\n')
        eachcontent.append('---')
        if clippingsCount == 0:
            eachcontent.append('\n\n<!-- more -->')
        clippingsCount = clippingsCount + 1
    eachcontent.append('\n')
    clippingsCount = '\n\n**共' + str(clippingsCount) + '条标注**\n'
    # 如果不需要标注计数，请把下一行前加#
    eachcontent.insert(2, clippingsCount)
    # 写入.md文件
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