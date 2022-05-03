from threading import Condition
class H2O:
    def __init__(self):
        self.cond = Condition()
        self.h = 0
        self.o = 0


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.cond:
            while self.h==2:
                self.cond.wait()
            self.h+=1

            releaseHydrogen()
            if self.h==2 and self.o==1:
                self.h = self.o = 0
            self.cond.notify()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.cond:
            while self.o==1:
                self.cond.wait()
            self.o+=1
            releaseOxygen()
            if self.h==2:
                self.h = self.o = 0
            self.cond.notify()

            