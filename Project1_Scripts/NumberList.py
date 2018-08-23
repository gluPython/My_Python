import string
#!/usr/bin/python
def write(arg1,arg2):
    file = open(arg1, 'a')
    file.write('\n'+arg2)
    file.close()
dir=r'C:\Users\Glu Tbl\Desktop\\NewFolder\a.txt'

for num in range(1,370100):
    print (num)
    write(dir,str(num))