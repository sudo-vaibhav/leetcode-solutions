class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        prev = 0
        f = finalSum
        ans = []
        if f%2==1: return []
        while f>0:
            now = prev+2
            if f-now<=now:
                ans.append(f)
                f-=f
            else:
                ans.append(now)
                f-=now
            prev = now
        return ans
                
        