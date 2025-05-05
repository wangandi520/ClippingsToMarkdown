# encoding:utf-8
# https://github.com/wangandi520/ClippingsToMarkdown
# Programmed by Andy
# Moon Reader Pro 9.0
# v0.5
# 2025.03.07
# 转换出的markdown文件直接可以在hexo里使用，一般放在hexo\source\_posts文件夹里

from pathlib import Path
import sys
import time
import re

# 把可以更改的设置都放在这里
CONFIG = {
    'toHexoMode': True,  # True: 转换成hexo博客的格式，False: 转换成一般markdown格式
    'tags': ['阅读', '标注', '读书笔记'],  # hexo博客的标签
    'categories': '读书笔记',  # hexo博客的分类
    'preview_notes': 2,  # 主页显示的标注数量
    'sort_by_location': True  # True: 按标注在书中的先后顺序，False: 按标注添加的时间顺序
}

def validFileName(oldFileName):
    # '/ \ : * ? " < > |'
    # 替换为下划线
    validChars = r"[\/\\\:\*\?\"\<\>\|]"  
    newFileName = re.sub(validChars, "", oldFileName)
    return newFileName
    
def readfile(filename: Path) -> list[str]:
    with open(filename, mode='r', encoding='UTF-8') as file:
        return [line.rstrip() for line in file]

def writefile(filename: Path, filereadlines: list[str]) -> None:
    # 写入.md文件
    newfile = open(Path(filename).parent.joinpath(Path(filename).stem + '标注.md'), mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    print('完成：' + str(Path(filename).name))
    
def convertMoonReadermrexpt(filename: Path) -> None:
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
    if CONFIG['sort_by_location']:
        allContentSorted = sorted(allContent, key=lambda x: (x[0]))
    else:
        allContentSorted = allContent
    # 输出
    outputContent = []
    # hexo文章头部信息Front-matter，title，tags，categories，time
    if CONFIG['toHexoMode']:
        myFrontMatter = '---\ntitle: ' + str(Path(filename).stem) + ' 标注\ntoc: true\ntags:\n- ' + '\n- '.join(CONFIG['tags']) + '\ncategories: \n- ' + CONFIG['categories'] + '\ndate: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n---\n\n'
    else:
        myFrontMatter = '## ' + str(Path(filename).stem) + '\n\n'
    outputContent.append(myFrontMatter)
    outputContent.append('**共' + str(len(allContentSorted)) + '条标注**\n\n---')
    for myIndex in range(0, len(allContentSorted)):
        outputContent.append('\n\n> ' + allContentSorted[myIndex][1] + '\n\n')
        if len(allContentSorted[myIndex]) == 4:
            outputContent.append('**' +allContentSorted[myIndex][2] + '**\n\n')
            outputContent.append('*' + allContentSorted[myIndex][3] + '*\n\n')
        elif len(allContentSorted[myIndex]) == 3:
            outputContent.append('*' +allContentSorted[myIndex][2] + '*\n\n')
        outputContent.append('---')
        # 在主页显示几条标注，显示2条myIndex == 1
        if myIndex == CONFIG['preview_notes'] - 1 and CONFIG['toHexoMode']:
            outputContent.append('\n\n<!-- more -->')
    # 写入.md文件
    writefile(validFileName(filename.name), outputContent)
    
def main(inputPath: list[str]) -> None:
    fileType = {'.mrexpt'}
    for eachPath in inputPath[1:]:
        eachPath = Path(eachPath)
        if Path.is_dir(eachPath):
            for eachFile in eachPath.glob('**/*'):
                if eachFile.suffix in fileType:
                    convertMoonReadermrexpt(eachFile)
        if Path.is_file(eachPath):
            if eachPath.suffix in fileType:
                convertMoonReadermrexpt(eachPath)
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
        else:
            print('请拖拽文件到本脚本，或者命令行运行时添加文件路径')
    except Exception as e:
        print(f"程序运行出错: {str(e)}")