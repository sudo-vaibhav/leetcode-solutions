class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m,n = map(len,[bank,bank[0]])
        
        ans = 0
        
        prev = 0
        
        for i in range(m):
            cur = 0
            for j in range(n):
                if bank[i][j]=="1":
                    cur+=1
            if cur!=0:
                ans += prev*cur
                prev = cur
        return ans