class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        stack = deque()
        ans = [0]*n
        for i in range(n-1,-1,-1):
            while stack and temps[stack[-1]]<=temps[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]-i
            stack.append(i)
        return ans
