class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        
        for i in range(len(nums)):
            
            cutoff = i-k
            if q and q[0][0]<=cutoff:
                q.popleft()
            while q and q[-1][1]<=nums[i]:
                q.pop()
            q.append((i,nums[i]))
            if i>=k-1:
                ans.append(q[0][1])
        return ans