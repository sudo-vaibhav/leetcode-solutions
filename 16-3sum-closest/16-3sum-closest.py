class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = inf
        ans = 0
        
        for i in range(n-2):
            j = i+1
            k = n-1
            
            while j<k:
                # print
                tot = nums[i]+nums[j]+nums[k]
                absDiff = abs(tot-target)
                if absDiff<=diff:
                    diff = absDiff
                    ans = tot
                if tot>target:
                    k-=1
                else:
                    j+=1
        
        return ans