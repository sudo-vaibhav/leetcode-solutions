class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        arr.sort()
        
        n = len(arr)+1
        last = arr[-1]
        first = arr[0]
        
        d = (last-first)//(n-1)
        
        
        for i in range(1,len(arr)):
            expectation = first+i*d
            if arr[i]!=expectation:
                return expectation
        return first
            