class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        n = len(arr)
        r = 0
        ans = 0
        while r<n:
            
            
            maxPosOfCur = arr[r]
            r = r+1
            
            while r<= maxPosOfCur:
                maxPosOfCur = max(maxPosOfCur,arr[r])
                r+=1
                
            ans+=1
            
        return ans