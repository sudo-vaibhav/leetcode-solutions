class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        vals = {0:0,1:1}
        if n==0:return 0
        i = 2
        while i<=n:
            
            if i%2==0:
                vals[i]=vals[i//2]
            else:
                vals[i]=vals[(i-1)//2]+vals[(i-1)//2+1]
            i+=1
        return max(vals.values())