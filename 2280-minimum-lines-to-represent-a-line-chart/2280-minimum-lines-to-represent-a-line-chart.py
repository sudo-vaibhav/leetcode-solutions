from fractions import Fraction
class Solution:
    def minimumLines(self, st: List[List[int]]) -> int:
        st.sort(key = lambda x:x[0])
        prev,n = inf,len(st)
        prevX,prevY = st[0]
        ans = 0
        for i in range(1,n):
            x,y = st[i]
            prevX,prevY = st[i-1]
            slope = Fraction(y-prevY,x-prevX)
            if slope!=prev:
                ans += 1
            prev = slope
        return ans