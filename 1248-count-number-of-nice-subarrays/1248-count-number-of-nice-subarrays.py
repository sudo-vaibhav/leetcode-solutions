class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oc = 0
        ct = defaultdict(int)
        ct[0]=1
        
        n = len(nums)
        ans = 0
        for i in range(n):
            cur = nums[i]
            
            if cur%2==1:
                oc+=1
            ct[oc]+=1
                
            f=oc-k
            ans+=ct[f]
                
        return ans