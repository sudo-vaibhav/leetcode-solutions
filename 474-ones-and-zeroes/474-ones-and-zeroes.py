class Solution:
    @cache
    def solve(self, N,m,n):
        if N == 0 : return 0
        if m == 0 and n==0: return 0
        
        curString = self.strs[N-1]
        counts = self.counts[curString]
        
        if counts[0]<=m and counts[1]<=n:
            return max(1 + self.solve(N-1,m-counts[0],n-counts[1]), self.solve(N-1,m,n))
        else:
            return self.solve(N-1,m,n)
        
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = {}
        for string in strs:
            zCount = 0
            for i in string:
                if i=='0':
                    zCount+=1
            
            counts[string] = {
                0 : zCount,
                1 : len(string) - zCount
            } 
        self.strs = strs  
        self.counts = counts
        return self.solve(len(strs),m,n)
        # return 2