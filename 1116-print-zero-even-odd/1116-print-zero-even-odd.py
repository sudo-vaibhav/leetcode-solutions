from math import ceil
from threading import Condition, Thread
import os
from typing import Callable

# def printNumber(num):
#     print(num,end="",flush=True)
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cv = Condition()
        self.printZero = True
        self.printOdd = True
        self.oi = 1
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            with self.cv:
                while not self.printZero:
                    self.cv.wait()
                printNumber(0)
                self.printZero = False
                self.cv.notify_all()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n//2):
            with self.cv:
                while self.printOdd or self.printZero:
                    self.cv.wait()
                printNumber(self.oi+1)
                self.oi+=2
                self.printZero = True
                self.printOdd = True
                self.cv.notify_all() 
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(ceil(self.n/2)):
            with self.cv:
                while (not self.printOdd) or self.printZero:
                    self.cv.wait()
                printNumber(self.oi)
                self.printZero = True
                self.printOdd = False
                self.cv.notify_all()
# N = 5     
# obj = ZeroEvenOdd(N)
# def f1():
#     for _ in range(N):
#         obj.zero(printNumber)
# def f2():
#     for _ in range(N//2):
#         obj.even(printNumber)
    
# def f3():
#     for _ in range(ceil(N/2)):
#         obj.odd(printNumber)
    
# t1,t2,t3 = Thread(target=f1),Thread(target=f2),Thread(target=f3)

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()