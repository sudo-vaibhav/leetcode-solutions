class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n<2:return False
        seen = defaultdict(lambda:inf)
        seen[nums[0]%k]=0
        temp = (nums[0]+nums[1])%k
        seen[temp]=min(1,seen[temp])
        running = nums[0]+nums[1]
        seen[0]=-1
        if sum(nums[:2])%k==0:return True
        for i in range(2,n):
            running+=nums[i]
            # print(running%k,seen)
            if seen[running%k]<i-1:
                return True
            seen[running%k]=min(seen[running%k],i)
        return False
            
            
            