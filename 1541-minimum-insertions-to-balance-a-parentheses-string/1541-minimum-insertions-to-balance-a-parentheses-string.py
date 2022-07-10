class Solution:
    def minInsertions(self, s: str) -> int:
        S = ""
        n = len(s)
        i = 0
        ans = 0
        while i<n:
            cur = s[i]
            if cur=="(":
                S+= cur
            else:
                if i+1<n and s[i+1]==")":
                    S+= cur
                    i+=1
                else:
                    S+=cur
                    ans+=1
            i+=1
        # print(S)
        st = deque()
        
        for i in range(len(S)):
            cur = S[i]
            if cur == "(":
                st.append(cur)
            else:
                if st:
                    st.pop()
                else:
                    ans+=1
                    
        return ans + len(st)*2