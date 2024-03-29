class Solution:
    def atmostSubarrays(self,nums,v,k):
        l = 0
        c = 0
        for r in range(len(nums)):
            if nums[r]==v:
                c+=1
            while c>k:
                if nums[l]==v:
                    c-=1
                l+=1
            
        
    def countSubarrays(self, nums: List[int], k: int) -> int:
        r = 0
        d = [0]
        v = max(nums)
        ans = 0
        for idx,i in enumerate(nums):
            if i==v:
                r+=1
            temp = r-k
            
            if temp>=0:
                x = bisect_right(d,temp)
                # print(temp,idx,i,x)
                ans += x
            d.append(r)
        return ans