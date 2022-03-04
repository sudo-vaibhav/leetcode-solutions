class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums)
        ans = set()
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                needed = -(nums[i]+nums[j])
                neededFreq = freq[needed]
                
                if(nums[i]==needed):
                    neededFreq-=1
                if(nums[j]==needed):
                    neededFreq-=1
                    
                if neededFreq>0:
                    ans.add(tuple(sorted((nums[i],nums[j],needed))))
        return list(ans)
                
                