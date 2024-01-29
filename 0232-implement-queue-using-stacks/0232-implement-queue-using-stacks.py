class MyQueue:

    def __init__(self):
        self.st = []
        self.st2 = []

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        while self.st:
            self.st2.append(self.st.pop())
        ans = self.st2.pop()
        while self.st2:
            self.st.append(self.st2.pop())
        return ans
    
    def peek(self) -> int:
        while self.st:
            self.st2.append(self.st.pop())
        ans = self.st2[-1]
        while self.st2:
            self.st.append(self.st2.pop())
        return ans

    def empty(self) -> bool:
        return len(self.st)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()