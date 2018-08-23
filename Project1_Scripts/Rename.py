import glob
import codecs
import random
def read_txt(arg1):#dont forget to import "codes" as it is required             used for the file

    data = open(arg1,'r').read().split('\n')
    #text = data.readlines()#read line by line and arrange in array
    print (data)
    #text = [s.replace('\r\n', '') for s in text]#replaing "\r\n" #doesnot remove next line
    #text= ''.join(text)# to convert in string
    ##print text
    return data

numberlist=read_txt(r'C:\Users\Glu Tbl\Desktop\nnnn\a.txt')


def rand(arg):
    x=random.choice(arg)
    print (x)
    arg.remove(x)
    return x




import shutil
dir=r'C:\Users\Glu Tbl\Desktop\word'
#print(glob.glob(r'C:\Users\Glu Tbl\Desktop\NewFolder\*.txt'))
x=glob.glob(r'C:\Users\Glu Tbl\Desktop\wrd\*.txt')
for y in x:
    print (y)
    ran = rand(numberlist)
    print (dir+r'\\'+ran+'.txt')


    shutil.move(y, dir+r'\\'+ran+'.txt')
print (numberlist)
