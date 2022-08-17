class Solution:

    def __init__(self, m: int, n: int):
        self.m,self.n = m,n
        self.used = set()

    def flip(self) -> List[int]:
        r = randint(0,self.m-1) 
        c = randint(0,self.n-1)
        
        while (r,c) in self.used:
            r = randint(0,self.m-1) 
            c = randint(0,self.n-1)
        
        self.used.add((r,c))
        return (r,c)
    
    def reset(self) -> None:
        self.used = set()
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()