class Solution(object):
    def longestValidParentheses(self, s):
        stack = deque()
        validSubstringDelimiters = []
        ans = 0

        for idx,char in enumerate(s):
            if char==")":
                if stack: # if it already has some opening parenthesis
                    stack.pop()
                else:
                    # else any valid substring wont have current char as a part (since this char will never be matched by anything)
                    validSubstringDelimiters.append(idx)
            else:
                # always add an opening parenthesis to stack
                stack.append(idx)

        # any unpopped opening parenthesis can also not be part of valid substring
        while stack:
            validSubstringDelimiters.append(stack.pop())
        
        # -1 and n are also valid delimiters and we need to account for these corner cases
        validSubstringDelimiters.extend([-1,len(s)])

        # sorting needed as two nearest invalid indices will have valid
        # substring in between them, only adjacent pairs need to be 
        # considered as non-adjacents will have an invalid character between them
        validSubstringDelimiters.sort()

        for i in range(1,len(validSubstringDelimiters)):
            prev = validSubstringDelimiters[i-1]
            cur  = validSubstringDelimiters[i]            
            ans = max(ans,cur-prev-1) # consider current substring length and store max possible val
        return ans