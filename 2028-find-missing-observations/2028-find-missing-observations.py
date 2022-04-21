class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        leftSum = mean*(m+n)-sum(rolls)
        ans = []
        while n>1:
            temp = ceil(leftSum/n)
            if temp>6 or temp<1:
                return []
            ans.append(temp)
            n-=1
            leftSum-=temp
        
        if leftSum>6 or leftSum<1 or int(leftSum)!=leftSum:
            return []
        ans.append(leftSum)
        n-=1
        return ans
                
        