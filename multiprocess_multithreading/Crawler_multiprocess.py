# coding=utf-8
# os ---> fork  Unix/Linux
# multiprocessing ---> Process  跨平台实现
import os
from multiprocessing import Process

""""  # 子进程要执行的代码
def run_proc(name): 
    print ('Child process %s (%s) Running...' % (name, os.getpid()))
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))  # 前面确定要调用的目标函数，后面为函数传递参数
        print('Process will start!')
        p.start()
    p.join()
    print('Process end.')
"""

from multiprocessing import Pool
import time, random

"""  # Pool类 进程池对象
def run_task(name):
    print('Task %s (pid = %s) is running...' % (name, os.getpid()))
    time.sleep(random.random() * 3)
    print('Task %s end.' % name)


if __name__ == '__main__':
    print('Current process %s .' % (os.getpid()))
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print('Waiting for all sub_processes done...')
    p.close()
    p.join()
    print('All subprocess done...')
"""

"""  # 进程间的通信交互
from multiprocessing import Process, Queue


def proc_write(q, urls):   # 写数据进程执行的代码
    print('Process(%s) is writing...' % (os.getpid()))
    for url in urls:
        q.put(url)
        print('Put %s to queue...' % (url))
        time.sleep(random.random())  # [0, 1)


def proc_read(q):  # 读数据进程执行的代码
    print('Process(%s) is reading...' % (os.getpid()))
    while True:
        url = q.get(True)
        print('Get %s from queue.' % url)


if __name__ == '__main__':  # 父进程创建Queue，并且传递给各个子进程
    q = Queue()
    proc_writer1 = Process(target=proc_write, args=(q, ['url_1', 'url_2', 'url_3']))
    proc_writer2 = Process(target=proc_write, args=(q, ['url_4', 'url_5', 'url_6']))
    proc_reader = Process(target=proc_read, args=(q,))

    proc_writer1.start()  # 启动子进程proc_writer,写入
    proc_writer2.start()

    proc_reader.start()  # 启动子进程proc_writer,读取

    proc_writer1.join()  # 等待proc_writer,结束
    proc_writer2.join()

    proc_reader.terminate()  # 进程里是死循环，无法等待其结束，只能强行终止
"""

"""  # Pipe 的通信机制
import multiprocessing
# import random


def proc_send(pipe, urls):
    for url in urls:
        print("Process (%s) send: %s" % (os.getpid(), url))
        pipe.send(url)
        time.sleep(random.random())


def proc_recv(pipe):
    while True:
        print("Process(%s) recv: %s" % (os.getpid(), pipe.recv()))
        time.sleep(random.random())


if __name__ == '__main__':
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc_send, args=(pipe[0], ['url_' + str(i) for i in range(10)]))
    p2 = multiprocessing.Process(target=proc_recv, args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.terminate()
"""