from threading import Lock, Condition

class FooBar:
    def __init__(self, n):
        self.fooPrint = True
        self.n = n
        lock = Lock()
        self.cond_var = Condition(lock)
        


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.cond_var.acquire()
            while not self.fooPrint:
                self.cond_var.wait()
            self.fooPrint = False
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.cond_var.notify()
            self.cond_var.release()
            


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.cond_var.acquire()
            while self.fooPrint:
                self.cond_var.wait()
            self.fooPrint = True
                
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.cond_var.notify()
            self.cond_var.release()