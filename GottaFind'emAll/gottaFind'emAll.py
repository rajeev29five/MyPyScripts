import re
import os
from termcolor import colored

def file_handling(path, pattern):

    if os.path.isfile(path):
        fileObj = open(path)
        lines = fileObj.readlines()
        regex = re.compile(r'%s' % pattern,re.I)
        lineNum = 1;
        for line in lines:
            mo = regex.findall(line)
            for exp in mo:
                if(mo != []):
                    lineItem = line.strip().split()
                    lineItem.append('\n')
                    print path," :line", lineNum, " ",
                    for word in lineItem:
                        if pattern.lower() in word.lower():
                            print colored(word,'red')," ",
                        elif word=='\n':
                            print word
                        else:
                            print word, " ",
            lineNum += 1
        fileObj.close()

def dir_handling(path, pattern):

    if(os.path.exists):
        listOfDir = os.listdir(path)
        for info in listOfDir:
            location = path+'/'+info
            if(os.path.isdir(location)):
                dir_handling(location, pattern)
            elif(os.path.isfile(location)):
                file_handling(location,pattern)
    else:
        print "Invalid Path"

dir_handling(raw_input("Enter the path of file: "),raw_input("Enter pattern for search: "))

