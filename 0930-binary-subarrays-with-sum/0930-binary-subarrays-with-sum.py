class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        running = 0
        
        seen = defaultdict(int)
        seen[0]=1
        ans = 0
        for i in nums:
            running+=i
            target = running-goal
            ans+=seen[target]
            seen[running]+=1
            
        return ans