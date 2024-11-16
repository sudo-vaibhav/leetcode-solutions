class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        q = deque([])
        
        n = len(nums)
        
        i = 0
        ans = []
        while i<n:
            cur = nums[i]
            
            if not q or cur<=q[-1] or cur>q[-1]+1:
                q = deque([cur])
            else:
                q.append(cur)
            if len(q)>k:
                q.popleft()
            if len(q)==k:
                ans.append(q[-1])
            elif i>=k-1:
                ans.append(-1)
            i+=1
        return ans