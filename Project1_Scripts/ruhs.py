enroll='C:\\Users\\Glu Tbl\\Desktop\\almerUC\\enroll.txt'
roll='C:\\Users\\Glu Tbl\\Desktop\\almerUC\\Roll.txt'
outputdir1='C:\\Users\\Glu Tbl\\Desktop\\almerUC\\nf\\foundRoll.txt'
outputdir2='C:\\Users\\Glu Tbl\\Desktop\\almerUC\\nf\\foundenRoll.txt'

import string
import requests

def read_txtln(arg1):
    with open(arg1) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        return content
def write(arg1,arg2):
    file = open(arg1, 'a')
    file.write('\n'+arg2)
    file.close()

Lroll=read_txtln(roll)
Lenroll=read_txtln(enroll)
print (Lroll[1])
length=''
n=0
m=len(Lroll)*len(Lenroll)
found=0
forloop=0

for numroll in Lroll[:]:
    m = len(Lroll) * len(Lenroll)
    forloop = forloop + 1
    for numenroll in Lenroll[:]:
        n=n+1


        r = requests.post("http://www.ruhsraj.org/results/view_resultsMBBS.php",data={'txtRollNo': numroll, 'txtEnRolYr': '2013', 'txtEnRolNo': numenroll, 'result_id': '360','submit': 'View+Results'})
        #print(r)
        #txtRollNo=200627&txtEnRolYr=2013&txtEnRolNo=2706&result_id=360&submit=View+Results
        if len(r.text)>12000:
            #length=length+"::::"+numenroll+" "+numroll+"    response:"+str(len(r.text))
            m = len(Lroll) * len(Lenroll)
            found=found+1
            Lenroll.remove(numenroll)

            print (numroll+"     "+numenroll)
            write(outputdir1,numroll)
            write(outputdir2,numenroll)
            forloop = 0
            break


        print (str(n) + '\\' + str(m)+   "     roll= "+numroll+"    enroll= "+numenroll + "     Res=  " + str(len(r.text))+"   loop=  "+ str(forloop)+ "  found:  "+str(found))
        #if forloop==250:
            #Lenroll.pop(0)
            #break
        #print str(found)+'  in  ' +str(n)+'\\'+str(m)
