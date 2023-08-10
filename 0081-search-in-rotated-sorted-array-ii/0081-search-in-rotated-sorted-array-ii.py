class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        n = len(nums)
        l,r = 0,n-1
        
        def isBinUseful(start,index):
            return not nums[start]==nums[index]
        
        while l<=r:
            m = (l+r)//2
            def isInFirstArray(start,val):
                return nums[start]<=val
            if nums[m]==target: return True
            if not isBinUseful(l,m):
                l+=1
                continue
            t_in_first,p_in_first = map(lambda x:isInFirstArray(l,x),[target,nums[m]]) 
            if t_in_first ^ p_in_first:
                if nums[m]<target:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m]>target:
                    r = m-1
                else:
                    l = m+1
                
            
        return False