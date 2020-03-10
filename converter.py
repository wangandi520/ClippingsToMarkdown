# -*- coding: UTF-8 -*-
def main():
    #read file
    file = open('source.txt', mode='r', encoding='UTF-8')
    alllines = file.readlines()

    #remove blank lines
    for i in alllines:
        if i == '\n':
            alllines.remove(i)
            
    #remove '\n' in line end
    for i in range(len(alllines)):
        alllines[i] = alllines[i].rstrip()
    
    #bookname,author style
    alllines[0] = '# ' + alllines[0]
    alllines[1] = '**' + alllines[1] + '**'

    #chapter,time,sentence style
    for i in range(2 , (len(alllines) - 3) , 3):
        alllines[i] = '## ' + alllines[i]
        alllines[i + 1] = '*' + alllines[i + 1] + '*'
        alllines[i + 2] =  '> ' + alllines[i + 2]
    alllines[len(alllines) - 1] = '**' + alllines[len(alllines) - 1][1:] + '**'
    
    #add blank lines
    for i in range(len(alllines)):
        alllines[i] = alllines[i] + '\n\n'

    #write file
    newfile = open('markdown.md', mode='w', encoding='UTF-8')
    newfile.writelines(alllines)

if __name__ == '__main__':
    main()