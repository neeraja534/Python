import threading
import time

1 usage new *
def square(num):
    for n in num:
        time.sleep(0.5)
        print("square: ",n*n)


2 usage new *
def cube(num):
    for n in num:
        time.sleep(0.7)
        print("cube=",n*n*n)

arr=[1,2,3,4]

t1=thraeding.Thread(target=square,args=(arr,))
t2=threading.Thread(target=square,args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()