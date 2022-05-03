    
from threading import Condition

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.cv = Condition()
        self.i = 1

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
    	while self.i<=self.n:
            with self.cv:
                while self.i<=self.n and not (self.i%3==0 and self.i%5!=0):
                    self.cv.wait()
                if self.i<=self.n:
                    printFizz()
                self.i+=1
                self.cv.notify_all()
                
            

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	while self.i<=self.n:
            with self.cv:
                while self.i<=self.n and not (self.i%3!=0 and self.i%5==0):
                    self.cv.wait()
                if self.i<=self.n:
                    printBuzz()
                self.i+=1
                self.cv.notify_all()
                

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while self.i<=self.n:
            with self.cv:
                while self.i<=self.n and not (self.i%3==0 and self.i%5==0):
                    self.cv.wait()
                if self.i<=self.n:
                    printFizzBuzz()
                self.i+=1
                self.cv.notify_all()
                
            
    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while self.i<=self.n:
            with self.cv:
                while self.i<=self.n and not (self.i%3!=0 and self.i%5!=0):
                    self.cv.wait()
                if self.i<=self.n:
                    printNumber(self.i)
                self.i+=1
                self.cv.notify_all()