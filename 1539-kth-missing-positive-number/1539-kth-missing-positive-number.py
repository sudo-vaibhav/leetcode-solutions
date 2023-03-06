class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        l,r = 0,len(arr)-1
        
        while l<=r:
            idx = (l+r)//2
            desiredVal = idx+1
            val = arr[idx]
            
            if val-desiredVal<k:
                l = idx+1
            else:
                r = idx-1
                
        return l+k
            