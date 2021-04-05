## 文石Boox,Kindle,静读天下专业版,微信读书,KOReader的标注转换为Markdown格式

*https://andi.wang/*

**基本用法(win10)**

安装python:[https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe](https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe)，复制你的标注到文件见，运行对应的py文件

**文石设备**

如果没有参数，就转换当前文件夹下的所有.txt文件为.md，不删除源文件。
如果有参数，就只转换那个文件
标注文件格式，在2020.03.13测试成功

**Kindle**

自动检测到My Clippings.txt
*如果你想保留原来的标注顺序，KindleSorted.py 改成 Kindle.py*
标注文件测试成功在2020.03.13(My Clippings.txt 文件在 2018.10.14 生成)
复制My Clippings.txt，运行KindleSorted.py

**静读天下专业版**

静读天下专业版中，书签，导出到文件，复制.mrexpt文件，运行MoonReaderPro.py

**微信读书**

我，笔记，书名，右上角，复制到剪贴板，复制到.txt文件中后运行WereadClippingsToMarkdown.py

**KOReader**

菜单，印象笔记，选中导出到本地json文件，点到处所有笔记，复制KOReaderClipping.json，运行KOReaderJsonALL.py。如果想每本书一个文件，请运行KOReaderJsonALLtoEachBook.py

---

## Boox,Kindle,Moon Reader pro,KOReader,Weread Clippings To Markdown

*https://andi.wang/*

**Basic usage(win10)**

install python:[https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe](https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe),copy your clipping file to folder,run .py

**Boox eink reader**

if with no arguments, it convert all .txt file in the folder(include subs)，origin .txt not deleted
if with arguments, it only convert the file to .md
origin clippings file tested succeed in 2020.03.13

**Kindle**

Auto detect kindle My Clippings.txt
if you dont's want the clippings sorted as book. Change KindleSorted.py to Kindle.py
origin clippings file tested in 2020.03.13(My Clippings.txt created in 2018.10.14)
copy My Clippings.txt,run KindleSorted.py

**Moon Reader pro**

In moon reader pro,bookmark, output to file,copy .mrexpt,run MoonReaderPro.py

**weread**

my,note,book,top right corner,copy to clipboard,copy contents to .txt and run WereadClippingsToMarkdown.py

**KOReader**

menu,Evernote,Export to local json files,Export all notes in your library，copy KOReaderClipping.json，run KOReaderJsonALL.py. If you want each book a .md file,please run KOReaderJsonALLtoEachBook.py