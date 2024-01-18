 ##new file
import time 
'''user = int(input('enter time to sleep: ')) + 1;
for i in range(1,user):
    print(i)
    time.sleep(1);
print("wake up"); '''
print(time.ctime(0)); ##epoch time from time 0
print(time.ctime(2000)); ##2000 seconds after epoch time
print(time.time()); ##will return current time in seconds

##blackbox
'''###to convert this into hours and minutes we can use the following code
hours = time.time() // 3600 #number of hours since epoch
minutes = (time.time() - hours * 3600) // 6
print("%d:%d" % (hours, minutes))'''

##current readable date
print(time.ctime(time.time())); ##epoch returns the time when the comp thinks time started, which accepts an argument, today's time in seconds

##another way to get current date
print(time.localtime());  #although this is not a readable format. 