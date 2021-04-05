## 将文石Boox、kindle、静读天下专业版的标注转换为markdown格式

*https://andi.wang/*

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

菜单，印象笔记，选中导出到本地json文件，点到处所有笔记，复制KOReaderClipping.json，运行KOReaderJsonALL.py

---

## Boox,Kindle,Moon Reader Clippings To Markdown

*https://andi.wang/*

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

menu,Evernote,Export to local json files,Export all notes in your library，copy KOReaderClipping.json，run KOReaderJsonALL.py