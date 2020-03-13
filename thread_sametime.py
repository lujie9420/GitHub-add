# @TIME : 2020/2/15 21:07
# @Author : lj
# @file : .py
import threading
import multiprocessing

# class i(threading.Thread):
#     def __init__(self, cond):
#         super().__init__(name='我')
#         self.cond = cond
#
#     def run(self):
#         with self.cond:
#             print(f'{self.name}说：在？')
#             self.cond.notify()
#             self.cond.wait()
#             print(f'{self.name}说：你在干嘛？')
#             self.cond.notify()
#
#
# class you(threading.Thread):
#     def __init__(self, cond):
#         super().__init__(name='你')
#         self.cond = cond
#
#     def run(self):
#         self.cond.acquire()
#         self.cond.wait()
#         print(f'{self.name}说：在，怎么了')
#         self.cond.notify()
#         self.cond.wait()
#         print(f'{self.name}说：这也是我想问你的')
#
#         self.cond.release()
#
#import threading
import multiprocessing
import greenlet

import requests
# 输入数据
# def fb1(pro):
#     try:
#         # 1/0
#         pro.put('i am putdata')
#     except Exception as e:
#         print(e)


# def fb2(pro):
#     try:
#
#         print(pro.get())
#     except Exception as e:
#         print(e)
#
#
# def main():
#     # cond = Queue() 普通队列 ，不能完成进程之间的通信
#     cond = multiprocessing.Queue()  # 跨进程通信的队列
#     pro = multiprocessing.Manager().Queue()  # 跨进程池之间的通信
#     pol = multiprocessing.Pool(3)
#     pooi = greenlet.greenlet(fb1)
#     t = pooi.switch()
#
#
#
#     pol.apply_async(fb1, args=(pro,))
#     pol.apply_async(fb2, args=(pro,))
#     pol.close()
#     pol.join()
# if __name__ == '__main__':
#     main()


# t1 = you(con)
#
# t1.start()
#
# t.start()








