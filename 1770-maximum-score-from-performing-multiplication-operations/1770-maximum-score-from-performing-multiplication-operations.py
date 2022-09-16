class Solution:
    def maximumScore(self, nums: List[int], mult: List[int]) -> int:
        N = len(nums)
        M = len(mult)
        
        @lru_cache(10000)
        def solve(startIdx,endIdx):
            taken = N - (endIdx-startIdx+1)
            leftToTake = M - taken
            if leftToTake==0: return 0 
            return max(mult[taken]*nums[startIdx] + solve(startIdx+1,endIdx),mult[taken]*nums[endIdx]+solve(startIdx,endIdx-1))
        
        return solve(0,N-1)
            