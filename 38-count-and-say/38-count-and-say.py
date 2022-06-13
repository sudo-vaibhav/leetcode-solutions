class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1: return "1"
        base = self.countAndSay(n-1)
        cur,r,cnt,N,ans = None,0,0,len(base),""
        while r<N:
            cur = base[r]
            while r<N and base[r]==cur:
                r+=1
                cnt+=1
            print(cur,cnt)
            ans+=str(cnt)+cur
            cnt=0
            
        return ans
            
            