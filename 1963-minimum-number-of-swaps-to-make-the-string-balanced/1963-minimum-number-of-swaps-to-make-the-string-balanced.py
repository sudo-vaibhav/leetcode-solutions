class Solution:
    def minSwaps(self, s: str) -> int:
        stack_size = 0
        for ch in s:
            # If character is opening bracket, increment the stack size.
            if ch == "[":
                stack_size += 1
            else:
                # If the character is closing bracket, and we have an opening bracket, decrease
                # the stack size.
                if stack_size > 0:
                    stack_size -= 1
        return (stack_size + 1) // 2