lines (74 sloc)  2.71 KB
 1) in alll .smali file you have to add .Source'SOMENAME' at the beginning if it was not added
 2) you need to add a smali class to call a static function
 3) calling the sttic function by adding  "invoke-static {}, Lcom/log/patch/logclass;->minithreadcode()V" i use this to know the thread number in .linenumber

 original java file of this is ====>

public static void minithreadcode()
 {
 try {
 Log.d("LOGGER MiniThread1", Thread.currentThread().getStackTrace()[3].toString());
 }catch (Exception e){Log.d("LOGGER Thread", "Exception e");}
 }
 do backsmaling and add class to the apk's smali folder'
 so that we can call form staticmethod
