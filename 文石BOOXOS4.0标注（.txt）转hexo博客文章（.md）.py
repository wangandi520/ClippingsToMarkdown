# encoding:utf-8
# https://github.com/wangandi520/ClippingsToMarkdown
# Programmed by Andy
# BOOX OS 4.0
# v0.1
# 2025.03.17
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

def getEachClippings(filename: Path) -> list[str]:
    groups = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            if not lines:
                return groups
            
            # 第一行作为第一组
            groups.append([lines[0].strip()])
            
            if len(lines) < 2:
                return groups
            
            # 第二行到第一个分隔符作为第二组
            current_group = []
            i = 1  # 从第二行开始
            
            # 处理第二组（第二行到第一个分隔符）
            while i < len(lines) and lines[i].strip() != "-------------------":
                current_group.append(lines[i].strip())
                i += 1
            
            if current_group:
                groups.append(current_group)
            
            # 跳过第一个分隔符
            if i < len(lines):
                i += 1
            
            # 处理剩余的组（每两个分隔符之间）
            current_group = []
            in_group = True
            
            while i < len(lines):
                line = lines[i].strip()
                
                if line == "-------------------":
                    if in_group:
                        # 当遇到分隔符且在组内时，结束当前组
                        if current_group:
                            groups.append(current_group)
                        current_group = []
                        in_group = False
                    else:
                        # 当遇到分隔符且不在组内时，开始新的一组
                        in_group = True
                elif in_group:
                    current_group.append(line)
                
                i += 1
            
            # 处理文件末尾可能的未完成组
            if in_group and current_group:
                groups.append(current_group)
                
    except FileNotFoundError:
        print("错误：1.txt 文件不存在")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
    
    return groups
    
def convertBooxTxt(filename: Path) -> None:
    # 读取.mrexpt文件
    # filereadlines = readfile(filename)
    print('处理：' + str(Path(filename).name))
    # 存储所有标注
    getAllClippings = []
    getAllClippings = getEachClippings(filename)
    # # 按照标注添加的时间顺序 = 1，order by time，还是按住标注所在书中的先后顺序 = 2，order by location，排列
    # if CONFIG['sort_by_location']:
        # allContentSorted = sorted(allContent, key=lambda x: (x[0]))
    # else:
        # allContentSorted = allContent
    # # 输出
    outputContent = []
    # hexo文章头部信息Front-matter，title，tags，categories，time
    if CONFIG['toHexoMode']:
        myFrontMatter = '---\ntitle: ' + getAllClippings[0][0][7:] + ' 标注\ntoc: true\ntags:\n- ' + '\n- '.join(CONFIG['tags']) + '\ncategories: \n- ' + CONFIG['categories'] + '\ndate: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n---\n\n'
    else:
        myFrontMatter = '## ' + getAllClippings[0][0][7:] + '\n\n'
    outputContent.append(myFrontMatter)
    outputContent.append('**共' + str(len(getAllClippings) - 1) + '条标注**\n\n---\n\n')
    for eachClippings in getAllClippings[1:]:
        startIndex = 0
        if '页码' not in eachClippings[0]:
            outputContent.append('## ' + eachClippings[0] + '\n\n')
            startIndex = 1
        for tempEach in range(startIndex, len(eachClippings)):
            if '页码' in eachClippings[tempEach]:
                outputContent.append('*' + eachClippings[tempEach] + '*\n\n')
            else:
                outputContent.append('> ' + eachClippings[tempEach] + '\n\n')
  
        outputContent.append('---\n\n')        
    # # 写入.md文件
    writefile(validFileName(getAllClippings[0][0][7:]), outputContent)
    
def main(inputPath: list[str]) -> None:
    fileType = {'.txt'}
    for eachPath in inputPath[1:]:
        eachPath = Path(eachPath)
        if Path.is_dir(eachPath):
            for eachFile in eachPath.glob('**/*'):
                if eachFile.suffix in fileType:
                    convertBooxTxt(eachFile)
        if Path.is_file(eachPath):
            print(eachPath)
            if eachPath.suffix in fileType:
                convertBooxTxt(eachPath)
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
        else:
            print('请拖拽文件到本脚本，或者命令行运行时添加文件路径')
    except Exception as e:
        print(f"程序运行出错: {str(e)}")