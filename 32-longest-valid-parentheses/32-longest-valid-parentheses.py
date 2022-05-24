class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = deque()
        invalids = []
        ans = 0
        
        for idx,char in enumerate(s):
            if char==")":
                if stack:
                    stack.pop()
                else:
                    invalids.append(idx)
            else:
                stack.append(idx)
                
        while stack:
            invalids.append(stack.pop())
        
        invalids.extend([-1,len(s)])
        invalids.sort()
        for i in range(1,len(invalids)):
            prev = invalids[i-1]
            cur  = invalids[i]
            
            ans = max(ans,cur-prev-1)
            
        # print(invalids)
            
        return ans
        