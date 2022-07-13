from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l,r = 0,0
        n = len(nums)
        window = SortedList()
        ans = 1
        while r<n:
            window.add(nums[r])
            while window[-1]-window[0]>limit:
                window.remove(nums[l])
                l+=1
            r+=1
            ans = max(ans,r-l)
        
        return ans