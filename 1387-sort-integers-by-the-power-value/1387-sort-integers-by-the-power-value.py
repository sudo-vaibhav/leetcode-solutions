class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def solve(x):
            if x<=2: return 0
            return 1 + (solve(x//2) if x%2==0 else solve(3*x+1))
        
        
        temp = list(range(lo,hi+1))
        
        temp.sort(key=lambda x:(solve(x),x))
        return temp[k-1]