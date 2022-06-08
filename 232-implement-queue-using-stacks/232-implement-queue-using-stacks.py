class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []
        

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        return self.st2.pop()
    
    def peek(self) -> int:
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        return self.st2[-1]

    def empty(self) -> bool:
        return not (self.st1 or self.st2)