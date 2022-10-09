from sortedcontainers import SortedList

class MaxStack:

    def __init__(self):
        self.stack = SortedList() # pushing order
        self.values = SortedList() # by value
        self.cnt = 0 # to give unique ids to each element

    def push(self, x: int) -> None:
        self.stack.add((self.cnt,x))
        self.values.add((x,self.cnt))
        self.cnt += 1
        
    def pop(self) -> int:
        idx,val = self.stack.pop()
        self.values.remove((val,idx))
        return val

    def top(self) -> int:
        return self.stack[-1][1]

    def peekMax(self) -> int:
        return self.values[-1][0]

    def popMax(self) -> int:
        val,idx = self.values.pop()
        self.stack.remove((idx,val))
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()