 ##new file
import time 
import threading
'''user = int(input('enter time to sleep: ')) + 1;
for i in range(1,user):
    print(i)
    time.sleep(1);
print("wake up"); '''

'''print(time.ctime(0)); ##epoch time from time 0
print(time.ctime(2000)); ##2000 seconds after epoch time
print(time.time()); ##will return current time in seconds'''

##blackbox
'''###to convert this into hours and minutes we can use the following code
hours = time.time() // 3600 #number of hours since epoch
minutes = (time.time() - hours * 3600) // 6
print("%d:%d" % (hours, minutes))'''

##current readable date
#print(time.ctime(time.time())); ##epoch returns the time when the comp thinks time started, which accepts an argument, today's time in seconds

##another way to get current date
#print(time.localtime());  #although this is not a readable format. 

'''##readable string format time, needs 2 arguments
##print(time.strftime(format,time-object)); #syntax for this method, you specify the format using identifiers, e.g
time_object = time.localtime()
local_time = time.strftime("%B %d %Y %H: %M: %S" , time_object) 
## B = month name, d=day, y=year, H = hour, M= month, S= second 
print(local_time)'''

####THREADING
'''#to print the number of threads running in the background
print(threading.active_count());
##to print a list of all the threads that are running we use
print(threading.enumerate());'''
##tasks to be done sequntially
def wake_Up():
    time.sleep(3) ##time it took for me cfinally wake up
    print("I'm awake now")
def breakfast():
    time.sleep(5) ##how long I take to eat my breakfat
    print("finished Breakfast")
def study():
    time.sleep(4)
    print("Finished studying")

'''we can have the three task running concurrently as if multitasking ----This is called Multithreading
currently we have one thread that is running these three functions, we can hav multiple threads, where each will be in
charge of each task, then we have our main  thread running in the background to complete the program, this is how we'll do it'''

t1 = threading.Thread(target=wake_Up, args=()); #you include the argument if the function has any
t1.start()
t2 = threading.Thread(target=breakfast, args=())
t2.start();
t3 = threading.Thread(target=study);
t3.start();
##this program with multiple threads will take a shorter time to complete, considering each thread has its own objective 
#to accomplish. The main one will not wait around for the other threads to complete their tasks.

###THREAD SYNCHRONIZATION
'''this is where our main thread waits around for other threads to synchronize and join, to complete their execution,
 for it to move on with its own instruction set, we use the join function'''
t1.join()
t2.join()
t3.join()
'''wake_Up()
breakfast()
study() '''
##these tasks will run sequentially
print(threading.active_count());
print(threading.enumerate)
print(time.perf_counter()) #will return the time it took for the main thread to complete its set of instruction

'''our main thread is not in charge of executing the three functions, but instead in charge of creating three additional
threads and then calling the active count function,the enumarate function and perf_counter function'''