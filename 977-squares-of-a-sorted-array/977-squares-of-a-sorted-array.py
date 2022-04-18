class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans,n = deque(),len(nums)
        l,r = 0,n-1
        while len(ans)<n:
            L,R = nums[l],nums[r]
            if abs(L)>abs(R):
                l+=1
                ans.appendleft(L**2)
            else:
                ans.appendleft(R**2)
                r-=1
        return ans