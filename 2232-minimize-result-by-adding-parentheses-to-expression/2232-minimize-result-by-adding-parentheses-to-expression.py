#         a,b = ex.split("+")
#         a = list(a)
#         b = list(b)
#         lp,rp = [],[]
#         for idx in range(len(a)):
#             lp.append(("".join(a[:idx]) or"1" ,"".join(a[idx:]) or "0"))
            
#         lp=[*lp,("".join(a),"0")]
#         for idx in range(len(b)):
#             rp.append(("".join(b[:idx+1]) or "1","".join(b[idx+1:]) or "1"))
#         rp = [("0","".join(b)),*rp,]
#         print(lp,rp)
        
#         m = 0
#         for u in lp:
#             u = list(map(int,u))
#             for v in rp:
#                 v = list(map(int,v))
#                 m = max(u[0]*(u[1]+v[0])*v[1],m)
#         # for j in enumerate(b):
#         return m
            
class Solution:
    def minimizeResult(self, ex: str) -> str:
        a,b = ex.split("+")
        # l = 0
        # r = len(b)-1
#         w*(X+Y)*Z
        ans ="" 
        m=inf
        for l in range(len(a)): # keep before
            W = int(a[:l] or "1")
            X = int(a[l:])
            for r in range(len(b)): # keep after
                Y = int(b[:r+1])
                Z = int(b[r+1:] or "1")
                temp = W*(X+Y)*Z
                m = min(temp,m)
                if m==temp:
                    ans = a[:l]+"("+str(a[l:])+"+"+str(b[:r+1])+")"+str(b[r+1:])
        return ans