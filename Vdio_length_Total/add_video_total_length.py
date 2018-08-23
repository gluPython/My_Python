import re
from functools import reduce
def read_txt(arg1):#dont forget to import "codes" as it is required             used for the file
    data = open(arg1,'r').read()
    return data

def video_min2Hour(arg1):#here we convert the 22:30 to hour decimal.. ege 10:30 to 10.50 hour
    # arg1=re.sub(':', '.', str(arg1))
    arg2=arg1.split(':')
    print (arg1)
    return (int(arg2[0])+int(arg2[1])/60)

def sum(arg1,arg2):
    return arg1+arg2


numberlist=read_txt(r'C:\Users\Glu Tbl\Desktop\folder\a.txt')
# print (numberlist)
myre = re.compile(r"\d+:\d\d", re.UNICODE)
filtre_num=myre.findall(numberlist)#here we find the number
filtre_num=list(map(video_min2Hour,filtre_num))#here we mak the string to int and also converted min to hour decimel
# arg1=re.sub(':', '.', str(filtre_num))
# reduce(sum,filtre_num)
print(reduce(sum,filtre_num))

########Following step is to convert into Hour and minut formate again#####
total=str(reduce(sum,filtre_num)).split('.')
# print(total[1][:2])
print("Total Time = %s Minute and %d Second"%(total[0],int(total[1][:2])*0.6))