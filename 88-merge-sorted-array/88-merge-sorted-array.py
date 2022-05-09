class Solution:
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = m-1,n-1
        k = n+m-1
        
        while j>=0:
            if i>=0 and a[i]>=b[j]:
                a[i],a[k] = a[k],a[i]
                i-=1
            else:
                b[j],a[k] = a[k],b[j]
                j-=1
            k-=1