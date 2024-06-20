import threading
import threading
import time
def square(n):
    for num in n:
        time.sleep(0.5)
        print(num*num)

def cube(n):
    for num in n:
        time.sleep(0.7)
        print(num*num*num)
arr=[1,2,3,4]
t1=threading.Thread(target=square,args=(arr,))
t2=threading.Thread(target=cube,args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()