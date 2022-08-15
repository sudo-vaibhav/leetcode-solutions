class Solution:
    def romanToInt(self, s: str) -> int:
        st = deque()
        
        valMap = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = 0
        for i in s:
            if not st or st[-1]>=valMap[i]:
                st.append(valMap[i])
            else:
                ans -= st[-1]
                st.pop()
                st.append(valMap[i])
        
        ans+=sum(st)
        return ans
                