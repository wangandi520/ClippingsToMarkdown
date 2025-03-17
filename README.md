## 博客原文

[静读天下MoonReaderPro，Kindle，KOReader，微信读书Weread标注转换为Markdown格式](https://andi.wang/2021/03/15/文石Boox,Kindle,静读天下专业版,微信读书,KOReader的标注转换为Markdown格式)

[部分书籍标注展示，多数使用MoonReaderProToMrexptForHexo.py](https://andi.wang/categories/%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0/)


## 静读天下MoonReaderPro，Kindle，KOReader，微信读书Weread标注转换为Markdown格式

**基本用法(win10)**

安装python:[https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe)，复制你的标注到文件夹，运行对应的py文件或者拖拽标注文件的py上

**静读天下专业版**

书签导出时选导出到文件(.mrexpt):MoonReaderProToMrexpt.py

静读天下专业版中，书签，导出到文件，复制.mrexpt文件，拖拽文件夹或.mrexpt到MoonReaderProToMrexpt.py

新版支持拖拽，支持标注添加的评论

书签导出时选分享高亮与备注(TXT), 后选total commander，保存成txt文件:MoonReaderProToTXT.py, MoonReaderPro7.0ToTXT.py

含章节信息，使用方法相同

静读天下专业版标注（.mrexpt）转hexo博客文章（.md).py，转换后的文件可以直接在Hexo博客里使用，'toHexoMode': False时也可以转换成普通的markdown格式

文件内CONFIG内可以设置：博客的标签，分类，主页显示的标注数量，按标注在书中的先后顺序或按标注添加的时间顺序

**Kindle**

自动检测到My Clippings.txt

*如果你想保留原来的标注顺序，KindleSorted.py 改成 Kindle.py*

标注文件测试成功在2020.03.13(My Clippings.txt 文件在 2018.10.14 生成)

复制My Clippings.txt，运行KindleSorted.py

**微信读书**

我，笔记，书名，右上角，复制到剪贴板，复制到.txt文件中后运行WereadClippingsToMarkdown.py

**KOReader**

菜单，印象笔记，选中导出到本地json文件，点到处所有笔记，复制KOReaderClipping.json，拖拽json或文件夹到KOReaderJsonALL.py。如果想每本书一个文件，请运行KOReaderJsonALLtoEachBook.py

新版支持拖拽

**文石设备**

2025.03.17更新BOOXOS 4.0脚本

使用trae协助编写

---

## Kindle,Moon Reader pro,KOReader,Weread Clippings To Markdown

*https://andi.wang/*

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
