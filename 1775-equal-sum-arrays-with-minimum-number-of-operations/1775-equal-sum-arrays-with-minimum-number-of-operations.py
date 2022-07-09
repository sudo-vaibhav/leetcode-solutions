class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        
        if m>n:
            m,n = n,m
            nums1,nums2 = nums2,nums1
        
        
        if 6*m < n:
            return -1
        s1,s2 = sum(nums1),sum(nums2)
        if s1>s2:return self.minOperations(nums2,nums1)
        
        nums1.sort()
        nums2.sort()
        i,j = 0,n-1
        
        ans = 0
        while s2>s1:
            l = nums1[i] if i<m else inf
            L = 6-l
            
            r = nums2[j] if j<n else inf
            R = r-1
            
            if L>R:
                i+=1
                s1+=L
            else:
                j-=1
                s2-=R
            ans+=1
        return ans
        