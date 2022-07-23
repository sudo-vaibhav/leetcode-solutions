class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        ans = ""
        taken = 0
        N = len(n)
        for j in range(N-1,-1,-1):
            if taken==3:
                ans = "."+ans
                taken = 0
            ans = n[j]+ans
            taken+=1
        
        return ans
        