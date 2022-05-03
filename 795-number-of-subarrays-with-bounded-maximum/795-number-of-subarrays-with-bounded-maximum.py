class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n,ans = len(nums),0
        # nextGreater = [n for _ in range(n)]
        prevGreater = [-1 for _ in range(n)]
        stack = deque()

        for i in range(n):
            cur = nums[i]
            while len(stack)>0 and nums[stack[-1]]<cur:
                stack.pop()
            
            if len(stack)>0:
                prevGreater[i] = stack[-1]
            stack.append(i)
        
        
        stack = deque()
        for j in range(n-1,-1,-1):
            cur = nums[j]
            temp = n
            while len(stack)>0 and nums[stack[-1]]<=cur:
                stack.pop()
            
            if len(stack)>0:
                temp = stack[-1]
                
            if left<=cur<=right:
                ls = j - prevGreater[j]
                rs = temp-j
                ans+= ls*rs
            stack.append(j)
            
        return ans