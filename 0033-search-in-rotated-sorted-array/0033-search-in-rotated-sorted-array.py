class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0,len(nums)-1
#       [4,5,6,0,1,2,3]
        
        while l<=r:
            m = (l+r)//2
            
            if nums[m]>nums[-1]:
                l = m+1
            else:
                r = m-1
        
        def bins(l,r):
            while l<=r:
                m = (l+r)//2
                if nums[m]==target: return m
                elif nums[m]>target:
                    r = m-1
                else:
                    l = m+1
            
        L,R = bins(0,l-1),bins(l,len(nums)-1)
        if L is not None:
            return L
        if R is not None:
            return R
        return -1