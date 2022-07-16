class Solution:
    def maxConsecutiveAnswers(self, ans: str, k: int) -> int:
        T,F = "T","F"
        
        def solve(toMake):
            cnt = {T:0,F:0}
            undesired = T if toMake==F else F
            l = 0
            res = 0
            for i in ans:
                cnt[i]+=1
                
                while l<len(ans) and cnt[undesired]>k:
                    cnt[ans[l]]-=1
                    l+=1
                
                res = max(res,sum(cnt.values()))
            return res
        
        return max(solve(T),solve(F))