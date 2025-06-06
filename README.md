## 博客原文

[静读天下MoonReaderPro，Kindle，KOReader，微信读书Weread标注转换为Markdown格式](https://andi.wang/2021/03/15/静读天下专业版标注转换为Markdown格式)

[部分书籍标注展示，多数使用MoonReaderProToMrexptForHexo.py](https://andi.wang/categories/%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0/)


## 静读天下MoonReaderPro，Kindle，KOReader，微信读书Weread标注转换为Markdown格式

### 基本用法(win10)

安装python:[https://www.python.org](https://www.python.org)，复制你的标注到文件夹，运行对应的py文件或者拖拽标注文件的py上

### 静读天下专业版

书签导出时选导出到文件，静读天下专业版标注（.mrexpt）转markdown或hexo（.md）.py

静读天下专业版中，书签，导出到文件，复制.mrexpt文件，拖拽文件夹或.mrexpt到.py文件上

静读天下专业版标注（.mrexpt）转hexo博客文章（.md).py，转换后的文件可以直接在Hexo博客里使用，'toHexoMode': False时也可以转换成普通的markdown格式

文件内CONFIG内可以设置：博客的标签，分类，主页显示的标注数量，按标注在书中的先后顺序或按标注添加的时间顺序

### 文石设备

2025.03.17更新BOOXOS 4.0脚本，文石BOOXOS4.0标注（.txt）转markdown或hexo（.md）.py

导出txt的方法：boox系统中阅读某本书，点击中间，左下目录，上方第三个按钮，左下角圆圈全选，右边按钮，导出到本地

### KOReader

koreader标注（.json）转markdown或hexo（.md）.py

导出koreader标注的方法：菜单第四项工具，导出标注，选择格式和服务，json。导出标注，导出本书所有笔记。

导出后的json文件位置在根目录koreader\clipboard

koreader-android-arm64-v2025.04版本测试通过

### Kindle

自动检测到My Clippings.txt

*如果你想保留原来的标注顺序，KindleSorted.py 改成 Kindle.py*

标注文件测试成功在2020.03.13(My Clippings.txt 文件在 2018.10.14 生成)

复制My Clippings.txt，运行KindleSorted.py

### 微信读书

我，笔记，书名，右上角，复制到剪贴板，复制到.txt文件中后运行WereadClippingsToMarkdown.py

---

## Kindle,Moon Reader pro,KOReader,Weread Clippings To Markdown

*https://andi.wang/*

**old english translation, not update**

**Basic usage(win10)**

install python:[https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe),copy your clipping file to folder,run .py or drag your file onto .py

**Moon Reader pro**
in bookmark, chose output to file(.mrexpt):MoonReaderProToMrexpt.py

In moon reader pro,bookmark, output to file, copy .mrexpt, drag .mrexpt or folder onto MoonReaderProToMrexpt.py

For Hexo blog, use MoonReaderProToMrexptForHexo.py

in bookmark, chose share clipping(TXT):MoonReaderProToTXT.py

copy contents to TXT file, same

**Kindle**

Auto detect kindle My Clippings.txt

if you dont's want the clippings sorted as book. Change KindleSorted.py to Kindle.py

origin clippings file tested in 2020.03.13(My Clippings.txt created in 2018.10.14)

copy My Clippings.txt,run KindleSorted.py

**weread**

my,note,book,top right corner,copy to clipboard,copy contents to .txt and run WereadClippingsToMarkdown.py

**KOReader**

menu,Evernote,Export to local json files,Export all notes in your library，copy KOReaderClipping.json，drag .json or folder to KOReaderJsonALL.py. If you want each book a .md file,please run KOReaderJsonALLtoEachBook.py

**Boox eink reader**

**boox script maybe not work, device is sold, update not sure**

if with no arguments, it convert all .txt file in the folder(include subs)，origin .txt not deleted

if with arguments, it only convert the file to .md

origin clippings file tested succeed in 2020.03.13

BooxLocalInternational.py for https://github.com/wangandi520/ClippingsToMarkdown/issues/1

BooxLocalInternational_anotherVersion.py https://github.com/wangandi520/ClippingsToMarkdown/issues/2
