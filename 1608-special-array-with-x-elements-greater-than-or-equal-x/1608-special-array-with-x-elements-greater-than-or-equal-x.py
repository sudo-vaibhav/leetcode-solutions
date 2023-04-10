class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 0,1000
        
        while l<=r:
            m = (l+r)//2
            
            temp = len(nums)-bisect_left(nums,m)
            if temp==m:
                return temp
            elif temp>m:
                l = m+1
            else:
                r=m-1
        
        return -1