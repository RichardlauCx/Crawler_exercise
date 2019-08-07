# -*- coding:utf-8 -*-
import time
import random
import threading

"""  # 创建线程方法一：
# def thread_run(urls):
#     print('Current %s is running...' % threading.current_thread().name)
#     for url in urls:
#         print('%s --->>> %s' % (threading.current_thread().name, url))
#         time.sleep(random.random())
#     print('%s ended.' % threading.current_thread().name)
# 
# 
# print('%s is running...' % threading.current_thread().name)
# t1 = threading.Thread(target=thread_run, name='Thread_1', args=(['url_1', 'url_2', 'url_3'],))
# t2 = threading.Thread(target=thread_run, name='thread_2', args=(['url_4', 'url_5', 'url_6'],))
# 
# t1.start()
# t2.start()
# t1.join()  # 如果一个线程在执行过程中要调用另外一个线程，并且等到其完成以后才能接着执行，那么在调用这个线程时可以使用被调用线程的join方法。
# t2.join()
# print('%s ended.' % threading.current_thread().name)
"""

"""  创建线程方法二:
class MyThreading(threading.Thread):  # 定义一个继承threading.Thread的子类，并重写run方法
    def __init__(self, name, urls):
        threading.Thread.__init__(self)  # 此类会自动调用run函数
        self.urls = urls
        self.name = name
        # #定义特殊方法__init__，即创建类的实例时，需要伴随传入类的属性值[即run方法中所需的参数]

    def run(self):
        print("Current %s is running..." % threading.current_thread().name)
        for url in self.urls:
            print('%s \n --->>>' % threading.current_thread().name)
            print('%s' % url)
            time.sleep(random.random())
        print('%s ended.' % threading.current_thread().name)


print('%s is running...' % threading.current_thread().name)
t1 = MyThreading(name='Thread_1', urls=['url_1', 'url_2', 'url_3'])
t2 = MyThreading(name='Thread_2', urls=['url_4', 'url_5', 'url_6'])
t1.start()
t2.start()
t1.join()
t2.join()
print('%s ended.' % threading.current_thread().name)
"""

mylock = threading.RLock()
num = 0


class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global num
        while True:
            mylock.acquire()
            print('%s locked, Number %d' % (threading.current_thread().name, num))
            if num >= 4:
                mylock.release()
                print('%s released, Number: %d' % (threading.current_thread().name, num))
                break
            num += 1
            print('%s released, Number: %s' % (threading.current_thread().name, num))
            mylock.release()


if __name__ == '__main__':
    thread_1 = MyThread('Thread_1')
    thread_2 = MyThread('Thread_2')
    thread_1.start()
    thread_2.start()