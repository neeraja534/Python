import threading
def cal_fun(n):
    print("thread",n)
#thread_t1=new_thread()
#t1=threading.Thread(target=function,args=array)
t1=threading.Thread(target=cal_fun,args=(10,))
t1.start()