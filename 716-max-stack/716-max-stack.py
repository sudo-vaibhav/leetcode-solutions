class MaxStack:

    def __init__(self):
        self.st = []
        self.maxSt = []

    def push(self, x: int) -> None:
        self.st.append(x)
        self.maxSt.append(max(x,(-inf if not self.maxSt else self.maxSt[-1])))

    def pop(self) -> int:
        self.maxSt.pop()
        return self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def peekMax(self) -> int:
        return self.maxSt[-1]

    def popMax(self) -> int:
        temp = []
        while self.st[-1]!=self.maxSt[-1]:
            temp.append(self.st.pop())
            self.maxSt.pop()
        ans = self.st.pop()
        self.maxSt.pop()
        while temp:
            self.push(temp.pop())
        return ans