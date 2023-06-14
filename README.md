## 文石Boox,Kindle,静读天下专业版,微信读书,KOReader的标注转换为Markdown格式

*https://andi.wang/*

*https://andi.wang/2021/03/15/%E6%96%87%E7%9F%B3Boox,Kindle,%E9%9D%99%E8%AF%BB%E5%A4%A9%E4%B8%8B%E4%B8%93%E4%B8%9A%E7%89%88,%E5%BE%AE%E4%BF%A1%E8%AF%BB%E4%B9%A6,KOReader%E7%9A%84%E6%A0%87%E6%B3%A8%E8%BD%AC%E6%8D%A2%E4%B8%BAMarkdown%E6%A0%BC%E5%BC%8F/*

**基本用法(win10)**

安装python:[https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe)，复制你的标注到文件夹，运行对应的py文件或者拖拽标注文件的py上

**文石设备**

如果没有参数，就转换当前文件夹下的所有.txt文件为.md，不删除源文件。

如果有参数，就只转换那个文件

只支持本地到处的标注，导出到印象笔记、onenote的暂不支持

标注文件格式，在2020.03.13测试成功

**Kindle**

自动检测到My Clippings.txt

*如果你想保留原来的标注顺序，KindleSorted.py 改成 Kindle.py*

标注文件测试成功在2020.03.13(My Clippings.txt 文件在 2018.10.14 生成)

复制My Clippings.txt，运行KindleSorted.py

**静读天下专业版**

书签导出时选导出到文件(.mrexpt):MoonReaderProToMrexpt.py

静读天下专业版中，书签，导出到文件，复制.mrexpt文件，拖拽文件夹或.mrexpt文件到MoonReaderPro.py

新版支持拖拽，支持标注添加的评论

书签导出时选分享高亮与备注(TXT), 后选total commander，保存成txt文件:MoonReaderProToTXT.py, MoonReaderPro7.0ToTXT.py

含章节信息，使用方法相同

**微信读书**

我，笔记，书名，右上角，复制到剪贴板，复制到.txt文件中后运行WereadClippingsToMarkdown.py

**KOReader**

菜单，印象笔记，选中导出到本地json文件，点到处所有笔记，复制KOReaderClipping.json，拖拽json或文件夹到KOReaderJsonALL.py。如果想每本书一个文件，请运行KOReaderJsonALLtoEachBook.py

新版支持拖拽

---

## Boox,Kindle,Moon Reader pro,KOReader,Weread Clippings To Markdown

*https://andi.wang/*

**Basic usage(win10)**

install python:[https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe),copy your clipping file to folder,run .py or drag your file onto .py

**Boox eink reader**

if with no arguments, it convert all .txt file in the folder(include subs)，origin .txt not deleted

if with arguments, it only convert the file to .md

origin clippings file tested succeed in 2020.03.13

BooxLocalInternational.py for https://github.com/wangandi520/ClippingsToMarkdown/issues/1

BooxLocalInternational_anotherVersion.py https://github.com/wangandi520/ClippingsToMarkdown/issues/2

**Kindle**

Auto detect kindle My Clippings.txt

if you dont's want the clippings sorted as book. Change KindleSorted.py to Kindle.py

origin clippings file tested in 2020.03.13(My Clippings.txt created in 2018.10.14)

copy My Clippings.txt,run KindleSorted.py

**Moon Reader pro**
in bookmark, chose output to file(.mrexpt):MoonReaderProToMrexpt.py

In moon reader pro,bookmark, output to file, copy .mrexpt, drag .mrexpt or folder onto MoonReaderPro.py

in bookmark, chose share clipping(TXT):MoonReaderProToTXT.py

copy contents to TXT file, same

**weread**

my,note,book,top right corner,copy to clipboard,copy contents to .txt and run WereadClippingsToMarkdown.py

**KOReader**

menu,Evernote,Export to local json files,Export all notes in your library，copy KOReaderClipping.json，drag .json or folder to KOReaderJsonALL.py. If you want each book a .md file,please run KOReaderJsonALLtoEachBook.py

