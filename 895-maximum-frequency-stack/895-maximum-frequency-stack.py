class FreqStack:
    
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxFreq = 0
    def push(self, val: int) -> None:
        self.freq[val] = self.freq[val]+1
        if self.freq[val]>self.maxFreq:
            self.maxFreq = self.freq[val]
        self.group[self.freq[val]].append(val)
        

    def pop(self) -> int:
        x = self.group[self.maxFreq].pop()
        self.freq[x]-=1
        if not self.group[self.maxFreq]:
            self.maxFreq-=1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()