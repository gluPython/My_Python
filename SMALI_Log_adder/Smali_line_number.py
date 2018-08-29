# 1) in alll .smali file you have to add .Source'SOMENAME' at the beginning if it was not added
# 2) you need to add a smali class to call a static function
# 3) calling the sttic function by adding  "invoke-static {}, Lcom/log/patch/logclass;->minithreadcode()V" i use this to know the thread number in .linenumber
#
# original java file of this is ====>
# ##################################
#  public static void minithreadcode()
# {
# try {
# Log.d("LOGGER MiniThread1", Thread.currentThread().getStackTrace()[3].toString());
# }catch (Exception e){Log.d("LOGGER Thread", "Exception e");}
# }
#
# ################################
# do backsmaling and add class to the apk's smali folder'
# so that we can call form staticmethod



import os
import re
import ntpath
import errno



def outputhfilepath(arg1):
    global mypath
    global myoutput
    arg1=arg1.replace(mypath,myoutput)
    return arg1

def writeme(arg1,filename):

    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(filename, "w") as f:
        f.write(arg1)


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def replace(match):
    global i
    i += 1
    return '\n    .line {0}\n    invoke-static {1}, Lcom/log/patch/logclass;->minithreadcode()V\n    '.format(i,"{}")

def strreplace(arg1):
    crs = open(arg1, "r")
    # print(crs)
    with open(arg1, 'r') as f:
        content = f.read()
    # print (content)
    contentnew=re.sub("\n    (?!(move-result.*?\n|\.local))", replace,content)
    print(contentnew)
    # arg2=path_leaf(arg1)
    # print(arg2)
    outputpathme=outputhfilepath(arg1)
    print (outputpathme)
    writeme(contentnew,outputpathme)

i=0
mypath='C:\\Users\\Glu Tbl\\Desktop\\smali\\input'
myoutput='C:\\Users\\Glu Tbl\\Desktop\\smali\\output'
pattern = "*.smali"
linenumber=1


# yolo='C:\\Users\\Glu Tbl\\Desktop\\smali\\input\\ijdv\\kjerje\\sefjib'
# print(outputhfilepath(yolo))


smalilist = [os.path.join(dp, f) for dp, dn, filenames in os.walk(mypath) for f in filenames if
             os.path.splitext(f)[1] == '.smali']#Getting all file detail including sub directoruies
# print(smalilist.__len__())
# strreplace(smalilist[0])
for smali in smalilist:
    # print(smali)
     strreplace(smali)


