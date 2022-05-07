class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = deque()
        n = len(nums)
        k = -inf
        for j in range(n-1,-1,-1):
            if nums[j]<k:
                return True
            
            while stack and stack[-1]<nums[j]:
                k = stack.pop()
                
            stack.append(nums[j])
        
        return False