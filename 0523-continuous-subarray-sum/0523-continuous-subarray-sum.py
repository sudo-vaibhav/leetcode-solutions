class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        seen = defaultdict(lambda:inf)
        seen[0] = -1
        prevRunning,curRunning=0,sum(nums[:2])
        if n>=2 and (curRunning%k==0): return True 
        for i in range(2,n):
            prev = i-2
            prevRunning+=nums[prev]
            curRunning+=nums[i]
            seen[prevRunning%k] = min(seen[prevRunning%k],prev)
            if seen[curRunning%k]<i-1:
                return True
        return False
            
            
            