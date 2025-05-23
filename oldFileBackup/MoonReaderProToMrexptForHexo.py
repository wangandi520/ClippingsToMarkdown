# encoding:utf-8
# https://github.com/wangandi520/ClippingsToMarkdown
# Programmed by Andy
# Moon Reader Pro 9.0
# v0.3
# 2024.02.08
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
    # 设置hexo文章头部信息Front-matter，title，tags，categories，time
    myFrontMatter = '---\ntitle: ' + str(Path(filename).stem) + ' 标注\ntoc: true\ntags:\n- ' + '\n- '.join(myTags) + '\ncategories: \n- ' + myCategories + '\ndate: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n---'
    # 读取.mrexpt文件
    filereadlines = readfile(filename)
    print('处理：' + str(Path(filename).name))
    # 存储所有标注
    allContent = []
    for i in range(4, len(filereadlines), 17):
        eachContent = []
        # filereadlines[i+4] = 第几章，从0开始，chapter
        # filereadlines[i+6] = 这一章内的位置，location in chapter
        eachContent.append([int(filereadlines[i+4]), int(filereadlines[i+6])])
        # 划线标注，underline clipping
        eachContent.append(filereadlines[i+12])
        # 手写的批注，input clipping
        if filereadlines[i+11] != '':
            eachContent.append(filereadlines[i+11])
        # 标注时间，time
        clippingTime = float(filereadlines[i+9])/1000
        clippingTimeTransfered = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(clippingTime))
        eachContent.append(clippingTimeTransfered)
        allContent.append(eachContent)
    # 按照标注添加的时间顺序 = 1，order by time，还是按住标注所在书中的先后顺序 = 2，order by location，排列
    getOrder = 2
    if getOrder == 2:
        allContentSorted = sorted(allContent, key=lambda x: (x[0]))
    else:
        allContentSorted = allContent
    # 输出
    outputContent = []
    outputContent.append(myFrontMatter)
    outputContent.append('\n\n**共' + str(len(allContentSorted)) + '条标注**\n\n---')
    for myIndex in range(0, len(allContentSorted)):
        outputContent.append('\n\n> ' + allContentSorted[myIndex][1] + '\n\n')
        if len(allContentSorted[myIndex]) == 4:
            outputContent.append('**' +allContentSorted[myIndex][2] + '**\n\n')
            outputContent.append('*' + allContentSorted[myIndex][3] + '*\n\n')
        elif len(allContentSorted[myIndex]) == 3:
            outputContent.append('*' +allContentSorted[myIndex][2] + '*\n\n')
        outputContent.append('---')
        # 在主页显示几条标注，显示2条myIndex == 1
        if myIndex == 1:
            outputContent.append('\n\n<!-- more -->')
    # 写入.md文件
    writefile(filename, outputContent)
    
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for eachFile in Path(aPath).glob('**/*'):
                if (Path(eachFile).suffix.lower() == '.mrexpt'):
                    convertMoonReadermrexpt(eachFile)
        if Path.is_file(Path(aPath)):
            if (Path(aPath).suffix.lower() == '.mrexpt'):
                convertMoonReadermrexpt(aPath)
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass