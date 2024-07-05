import threading
import time.sleep(0.5)
print("square=",n*n)
def f_square(n):
    print("Square=",n*n)
def f_cube(m):
for print("Cube=",n*n*n)
t1=threading.Thread(target=f_square,args=(5,))
t2=threading.Thread(target=f_cube,args=(10,))
t1.start()
t2.start()
t1.join()
t2.join()





