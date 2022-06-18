class Logger:

    def __init__(self):
        self.lastUsed = defaultdict(lambda : -inf)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        last = self.lastUsed[message]
        if last+10<=timestamp:
            self.lastUsed[message] = timestamp
            return True
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)