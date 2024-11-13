from sortedcontainers import SortedList
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        
        ans = 0
        
        s = SortedList([nums[0]])
        
        for i in nums[1:]:
            l = lower-i
            h = upper-i
            ans+=s.bisect_right(h)-s.bisect_left(l)
            s.add(i)
        return ans