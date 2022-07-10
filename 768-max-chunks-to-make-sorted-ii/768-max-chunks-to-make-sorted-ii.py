class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        positions = defaultdict(list)
        r = 0
        SORTED = sorted(arr)
        for i in range(n-1,-1,-1):
            positions[SORTED[i]].append(i)
        
        while r<n:
            
            lastIndex = positions[arr[r]].pop()
            
            i = r+1
            while i<= lastIndex:
                lastIndex = max(lastIndex,positions[arr[i]].pop())
                i+=1
            ans+=1
            r = i
        
        return ans