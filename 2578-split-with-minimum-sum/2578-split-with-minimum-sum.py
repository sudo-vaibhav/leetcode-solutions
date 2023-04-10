class Solution:
    def splitNum(self, num: int) -> int:
        num = str(num)
        ans = inf
        def solve(i,taken=[]):
            nonlocal ans
            if i==len(num):
                if 0<len(taken)<len(num):
                    nottaken = [i for i in range(len(num)) if i not in taken]
                    v1 = [num[i] for i in taken]
                    v2 = [num[i] for i in nottaken]
                    v1,v2 = map(lambda x:int("".join(sorted(x))),[v1,v2])
                    ans = min(ans,v1+v2)
            else:
                solve(i+1,taken)
                solve(i+1,[*taken,i])
            
                
            
            
        solve(0)
        return ans