class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        c = 0
        st = []
        for i in s:
            if i in "()":
                if i==")":
                    if c>0:
                        st.append(")")
                        c-=1
                else:
                    st.append("(")
                    c+=1
            else:
                st.append(i)
        final = []  
        while st:
            if st[-1] == "(" and c:
                c-=1
                # st.pop()
        # elif i==")":
            else:
                final.append(st[-1])
            st.pop()
        
        return "".join(reversed(final))