dir1=r'C:\Users\Glu Tbl\Desktop\\nnnn\a.txt'
dir2=r'C:\Users\Glu Tbl\Desktop\\nnnn\l.txt'

def read_txt(arg1):#dont forget to import "codes" as it is required             used for the file

    data = open(arg1,'r').read().split('\n')
    #text = data.readlines()#read line by line and arrange in array
    print (data)
    #text = [s.replace('\r\n', '') for s in text]#replaing "\r\n" #doesnot remove next line
    #text= ''.join(text)# to convert in string
    ##print text
    return data

x=read_txt(dir1)
y=read_txt(dir2)

for wrds in y:
    print (wrds)
    try:
        x.remove(wrds)
    except:
        print ("This is an error message!")

    print (len(x))
    print(">>>>")

print (x)