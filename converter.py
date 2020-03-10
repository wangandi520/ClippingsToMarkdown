# -*- coding: UTF-8 -*-
def main():
    file = open('source.txt', mode='r', encoding='UTF-8')
    alllines = file.readlines()

    for i in range(len(alllines)):
        alllines[i] = alllines[i].rstrip('\n')

    alllines[0] = '# ' + alllines[0]
    alllines[1] = '**' + alllines[1] + '**'

    for i in range(2 , (len(alllines) - 3) , 3):
        alllines[i] = '## ' + alllines[i]
        alllines[i + 1] = '*' + alllines[i + 1] + '*'
        alllines[i + 2] =  '> ' + alllines[i + 2]
    alllines[len(alllines) - 1] = '**' + alllines[len(alllines) - 1][1:] + '**'
    
    for i in range(len(alllines)):
        alllines[i] = alllines[i] + '\n\n'

    newfile = open('markdown.md', mode='w', encoding='UTF-8')
    newfile.writelines(alllines)

if __name__ == '__main__':
    main()