class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        pair = {"]":"[","}":"{",")":"("}
        for c in s:
            if c in "[({":
                st.append(c)
            else:
                if len(st)==0 or st[-1]!=pair[c]:
                    return False
                st.pop()
        
        return len(st)==0