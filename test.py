
import os
import time

# pull first 

for i in range (1,5000):

    # push 
    f = time.sleep(5) 
    os.system(r"C:\Users\test\Desktop\test\test\m.bat")

    # pull
    os.system(r"C:\Users\test\Desktop\test\test\pull.bat")
    f = time.sleep(5)    # pauses for 5 seconds
    o = open("test1.py", "w")
    o.write("{} print('This is a Django Rest Framework project')".format(i))





