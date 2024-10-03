class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        
        k = s%p
        # [3,1,4,2]
        # (-1) -> 0
        # 3 -> 3
        # 4 -> 4
        # 8 -> 2
        # 10 -> 4
        
        """
        7
        6,3,5,2
        6,0,5,7
        """
        # print()
        seen = {0:-1}
        r = 0
        if k==0:
            return 0
        ans = len(nums)
        for idx, num in enumerate(nums):
            r = (r+num)%p
            left = (r-k+p)%p
            # print(r,num,idx,left,seen)
            if left in seen:
                ans = min(ans,idx-seen[left])
            seen[r%p] = idx
        if ans==len(nums):
            return -1
        return ans