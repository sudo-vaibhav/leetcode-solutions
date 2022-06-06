class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1),len(nums2)
        tot = m+n
        onLeft = (m+n+1)//2
        l,r = 0,m
        
        while l<=r:
            takenFromFirst = l+(r-l)//2
            takenFromSecond = onLeft - takenFromFirst
            
            if takenFromSecond>n:
                l = takenFromFirst+1
                continue
            elif takenFromSecond<0:
                r = takenFromFirst-1
                continue
                
            l1 = -inf if takenFromFirst==0 else nums1[takenFromFirst-1]
            l2 = -inf if takenFromSecond==0 else nums2[takenFromSecond-1]
            
            r1 = inf if takenFromFirst==m else nums1[takenFromFirst]
            r2 = inf if takenFromSecond==n else nums2[takenFromSecond]
            
            if l1<=r2 and l2<=r1:
                if tot%2==0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
            else:
                if l1>r2:
                    r = takenFromFirst-1
                else:
                    l = takenFromFirst+1
        
        return 0