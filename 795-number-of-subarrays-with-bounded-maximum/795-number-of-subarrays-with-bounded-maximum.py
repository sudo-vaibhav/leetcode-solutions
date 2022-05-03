class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        
        nextGreater = [n for _ in range(n)]
        prevGreater = [-1 for _ in range(n)]
        
        stack = deque()
#         populating prev greater

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
            while len(stack)>0 and nums[stack[-1]]<=cur:
                stack.pop()
            
            if len(stack)>0:
                nextGreater[j] = stack[-1]
            stack.append(j)
        ans=0
        for i in range(n):
            cur = nums[i]
            if left<=cur<=right:
                ls = i - prevGreater[i] - 1
                rs = nextGreater[i]-i-1
                ans+= (ls+1)*(rs+1)
        # print(prevGreater)
        # print(nextGreater)
        
        return ans