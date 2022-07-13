class Solution:
    def longestDupSubstring(self, s: str) -> str:
#         try sliding window rolling hash + binary search
        n = len(s)
        s = [ord(i)-ord("a") for i in s]
        l,r = 1,n-1
        ans = ""
        MOD = 2**63-1
        base = 26
        def dupExists(ws):
            initHash = reduce(lambda x,y: (x*base+y)%MOD,s[:ws],0)
            seen = set()
            seen.add(initHash)
            leftmostPower = pow(base,ws-1,MOD)
            rolling = initHash
            for i in range(ws,n):
                rolling = (rolling-s[i-ws]*leftmostPower)%MOD
                rolling = (rolling*base)%MOD
                rolling = (rolling+s[i])%MOD
                if rolling in seen:
                    return s[i+1-ws:i+1]
                seen.add(rolling)
            return False
        while l<=r:
            m = l+(r-l)//2
            
            temp = dupExists(m) 
            if temp:
                ans = temp
                l = m+1
            else:
                r = m-1
        
        return "".join([chr(i+ord("a")) for i in ans])
            
        
        