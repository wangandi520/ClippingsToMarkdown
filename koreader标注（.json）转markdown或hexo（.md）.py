# encoding:utf-8
# https://github.com/wangandi520/ClippingsToMarkdown
# Programmed by Andy
# koreader-android-arm64-v2025.04
# v0.2
# 2025.05.05
# 导出koreader标注的方法：菜单第四项工具，导出标注，选择格式和服务，json。导出标注，导出本书所有笔记。
# 导出后的json文件位置在根目录koreader\clipboard
# 转换出的markdown文件直接可以在hexo里使用，一般放在hexo\source\_posts文件夹里

from pathlib import Path
import sys
import time
import re
import json
import datetime

# 把可以更改的设置都放在这里
CONFIG = {
    'toHexoMode': True,  # True: 转换成hexo博客的格式，False: 转换成一般markdown格式
    'tags': ['阅读', '标注', '读书笔记'],  # hexo博客的标签
    'categories': '读书笔记',  # hexo博客的分类
    'preview_notes': 2,  # 主页显示的标注数量
    'showChapterAndPage': False  # True: 在标注中显示章节和页数，False: 不显示
}

def validFileName(oldFileName):
    # '/ \ : * ? " < > |'
    # 替换为下划线
    validChars = r"[\/\\\:\*\?\"\<\>\|]"  
    newFileName = re.sub(validChars, "", oldFileName)
    return newFileName
    
def readJsonFile(filename: Path) -> list[str]:
    with open(filename, mode='r', encoding='UTF-8') as file:
        return json.load(file)
        
def readfile(filename: Path) -> list[str]:
    with open(filename, mode='r', encoding='UTF-8') as file:
        return [line.rstrip() for line in file]

def writefile(filename: Path, filereadlines: list[str]) -> None:
    # 写入.md文件
    newfile = open(Path(filename).parent.joinpath(Path(filename).stem + '标注.md'), mode='w', encoding='UTF-8')
    newfile.writelines(filereadlines)
    newfile.close()
    print('完成：' + str(Path(filename).name))
    
def convertKoreaderJson(filename: Path) -> None:
    # 读取.json文件
    jsonData = readJsonFile(filename)
    print('处理：' + str(Path(filename).name))
    outputContent = []
    # hexo文章头部信息Front-matter，title，tags，categories，time
    if CONFIG['toHexoMode']:
        myFrontMatter = '---\ntitle: ' + jsonData['title'] + ' 标注\ntoc: true\ntags:\n- ' + '\n- '.join(CONFIG['tags']) + '\ncategories: \n- ' + CONFIG['categories'] + '\ndate: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n---\n\n'
    else:
        myFrontMatter = '## ' + jsonData['entries'] + '\n\n'
    outputContent.append(myFrontMatter)
    outputContent.append('**共' + str(len(jsonData['entries'])) + '条标注**\n\n---')
    for myIndex in range(0, len(jsonData['entries'])):
        outputContent.append('\n\n> ' + jsonData['entries'][myIndex]['text'] + '\n\n')
        if 'note' in jsonData['entries'][myIndex] and jsonData['entries'][myIndex]['note'] != '':
            outputContent.append('**' + jsonData['entries'][myIndex]['note'] + '**\n\n')
        outputContent.append('*' + time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(jsonData['entries'][myIndex]['time'])) + '*')
        # 章节和页数
        if CONFIG['showChapterAndPage']:
            outputContent.append('\n\n*' + jsonData['entries'][myIndex]['chapter'] + '章 ' + str(jsonData['entries'][myIndex]['page']) + '页*')
        # 在主页显示几条标注
        if myIndex == CONFIG['preview_notes'] - 1 and CONFIG['toHexoMode']:
            outputContent.append('\n\n<!-- more -->')
        # 标注内容在同一章节内，只显示一条分割线
        if myIndex < len(jsonData['entries']) - 1 and jsonData['entries'][myIndex]['chapter'] != jsonData['entries'][myIndex + 1]['chapter']:
            outputContent.append('\n\n---')
    outputContent.append('\n\n---')
        # 在主页显示几条标注，显示2条myIndex == 1
    # 写入.md文件
    writefile(validFileName(filename.name), outputContent)

def main(inputPath: list[str]) -> None:
    fileType = {'.json'}
    for eachPath in inputPath[1:]:
        eachPath = Path(eachPath)
        if Path.is_dir(eachPath):
            for eachFile in eachPath.glob('**/*'):
                if eachFile.suffix in fileType:
                    convertKoreaderJson(eachFile)
        if Path.is_file(eachPath):
            if eachPath.suffix in fileType:
                convertKoreaderJson(eachPath)
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
        else:
            print('请拖拽文件到本脚本，或者命令行运行时添加文件路径')
    except Exception as e:
        print(f"程序运行出错: {str(e)}")