class BrowserHistory:
    def __init__(self, homepage: str):
        self.f = []
        self.b = []
        self.b.append(homepage)
        
    def visit(self, url: str) -> None:
        self.b.append(url)
        self.f = []

    def back(self, steps: int) -> str:
        for i in range(steps):
            if len(self.b)>1:
                self.f.append(self.b.pop())
        return self.b[-1]
    
    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.f:
                self.b.append(self.f.pop())
        return self.b[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)