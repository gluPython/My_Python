import glob
import ntpath

def dothis(string):
    read_line=read_txtln(string)
    # print(read_line)
    filename=path_leaf(string)
    # print("Filenae="+path_leaf(string))
    for x in read_line:
        addedline=x+border+filename
        print(addedline)
        write(diroutput+filename,addedline)

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
 
def read_txtln(arg1):
    with open(arg1) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        return content

def write(arg1,arg2):
    file = open(arg1, 'a')
    file.write('\n'+arg2)
    file.close()


dir=r'C:\Users\Glu Tbl\Desktop\files\input\\'
diroutput=r'C:\Users\Glu Tbl\Desktop\files\output\\'
fileextension=".java"
border="                                             //"
filelist=(glob.glob(dir+"*"+fileextension))
print(filelist[0])

for x in filelist:
    dothis(x)
