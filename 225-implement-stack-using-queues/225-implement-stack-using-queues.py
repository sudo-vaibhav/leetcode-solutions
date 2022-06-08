class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        
    def size(self):
        return len(self.q)
    
    def pop(self) -> int:
        n = self.size()
        for _ in range(n-1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        n = self.size()
        for _ in range(n-1):
            self.q.append(self.q.popleft())
        temp = self.q.popleft()
        self.q.append(temp)
        return temp


    def empty(self) -> bool:
        return self.size()==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()