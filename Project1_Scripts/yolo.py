import glob
x=glob.glob(r'C:\Users\Glu Tbl\Desktop\word\*.txt')

def write(arg1,arg2):
    file = open(arg1, 'a')
    file.write('\n'+arg2)
    file.close()
dir=r'C:\Users\Glu Tbl\Desktop\\nnnn\l.txt'
for num in x:
    print (num)
    write(dir,str(num)+"\r\n")