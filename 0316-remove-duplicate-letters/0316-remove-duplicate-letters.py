class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        @cache
        def isPresentAtAndAhead(i,c):
            if i==n: return False
            return c==s[i] or isPresentAtAndAhead(i+1,c)
        
        st = []
        present = set()
        for idx,c in enumerate(s):
            if c not in present:
                while st and st[-1]>c and isPresentAtAndAhead(idx+1,st[-1]):
                    present.remove(st.pop())
                # if c not in present:
                st.append(c)
                present.add(c)
        return "".join(st)