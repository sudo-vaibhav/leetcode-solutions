class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i=j=0
        n=len(pushed)
        st = []
        while j<n:
            while i<n and (not st or st[-1]!=popped[j]):
                st.append(pushed[i])
                i+=1
            if st and st[-1]==popped[j]:
                # s.remove(popped[j])
                st.pop()
                j+=1
            else:
                return False
        return True