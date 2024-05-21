class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        
        def solve(i,soFar=[]):
            if i==len(nums):
                ans.append(list(soFar))
                return
            solve(i+1,soFar)
            soFar.append(nums[i])
            solve(i+1,soFar)
            soFar.pop()
        solve(0,[])
        return ans