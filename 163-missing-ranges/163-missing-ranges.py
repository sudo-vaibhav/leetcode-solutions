class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [i for i in nums if lower<=i and  i<=upper]
        # nums.sort()
        ans = []
        def add(l,r):
            if l==r:
                ans.append(str(l))
            else:
                ans.append(str(l)+"->"+str(r))
        if not nums:
            add(lower,upper)
            return ans
        prev = lower
        for idx,i in enumerate(nums):
            if idx==0:
                if i!=lower:
                    add(prev,i-1)
            elif i-prev>1:
                add(prev+1,i-1)
            prev = i
            
        if prev!=upper:
            add(prev+1,upper)
        return ans
            