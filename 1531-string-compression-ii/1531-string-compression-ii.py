class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        N = len(s)
        
        def getCnt(prevChar,prevCnt):
            if prevCnt<=1: return prevCnt
            else: 
                temp = prevChar+str(prevCnt)
                # print("finished string",temp)
                return len(temp)
        @cache
        def solve(i,kVal,prevChar,prevCnt):
            # print(i,kVal,prevChar,prevCnt)
            # if kVal<0: return inf
            if i==N:
                temp = getCnt(prevChar,prevCnt)
                # print("string over returning",temp,prevChar,prevCnt)
                return temp
            else:
                cur = s[i]
                if cur==prevChar:
                    ans = solve(i+1,kVal,cur,prevCnt+1)
                    if kVal>0:
                        ans = min(ans,solve(i+1,kVal-1,cur,prevCnt))
                    return ans
                else:
                    temp = getCnt(prevChar,prevCnt) 
                    ans = temp + solve(i+1,kVal,cur,1)
                    if kVal>0:
                        ans = min(ans,solve(i+1,kVal-1,prevChar,prevCnt))
                    return ans
        
        return solve(0,k,"",0)
            