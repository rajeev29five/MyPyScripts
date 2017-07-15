import re
import os
from termcolor import colored


'''Ignore reading files with these extensions'''

ignoreList = ['.mp4','.avi','.mkv','.png','.jpg', '.jpeg', '.pdf','.mp3','.gif','.class', '.pyc']


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
                    print "[",path,"]"," :line", lineNum, " ",
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
        for l in listOfDir:
            flag = False
            for i in ignoreList:
                if l.lower().endswith(i.lower()) and os.path.isdir("./%s" % l) != True:
                    flag = True
                    break
                else:
                    flag = False
            if flag == True:
                continue
            else:
                #for info in listOfDir:
                location = path+'/'+l
                if(os.path.isdir(location)):
                    dir_handling(location, pattern)
                elif(os.path.isfile(location)):
                    file_handling(location,pattern)
    else:
        print "Invalid Path"


print "Example : /root/Documents/Projects"
print "-"*40

dir_handling(raw_input("Enter the path of file: "),raw_input("Enter pattern for search: "))

