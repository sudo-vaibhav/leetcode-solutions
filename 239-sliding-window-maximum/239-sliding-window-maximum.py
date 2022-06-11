class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q,ans = deque(),[]
        
        for idx,num in enumerate(nums):
            while q and idx-q[0][0]==k:
                q.popleft()
            while q and q[-1][1]<=num:
                q.pop()
            q.append((idx,num))
            if idx>=k-1:
                ans.append(q[0][1])
        return ans