class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        ans = 0
        for i in s:
            if i=="(":
                st.append(i)
            elif st:
                
                st.pop()
            else:
                ans +=1 
        return len(st)+ans