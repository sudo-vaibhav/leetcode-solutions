from threading import Condition

class DiningPhilosophers:
    def __init__(self):
        self.eatingForks = [Condition() for i in range(5)]
        
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   phil: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        lower,higher = (phil)%5,(phil+1)%5
        if lower>higher:
            lower,higher = higher,lower
            
        lf = self.eatingForks[lower]
        rf = self.eatingForks[higher]
        
        with lf:
            with rf:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
