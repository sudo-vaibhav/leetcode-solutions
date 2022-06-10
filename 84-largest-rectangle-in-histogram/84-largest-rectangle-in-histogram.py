class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        st = deque()
        # def getNextSmaller(arr,init):
        nextSmaller = [n]*n
        for i in range(n-1,-1,-1):
            while st and heights[st[-1]]>=heights[i]:
                st.pop()
            if st:
                nextSmaller[i]=st[-1]
            st.append(i)
        # return nextSmaller
        prevSmaller = [-1 for i in range(n)]
        st = []
        for i in range(n):
            while st and heights[st[-1]]>=heights[i]:
                st.pop()
            if st:
                prevSmaller[i] = st[-1]
            st.append(i)
        ans = 0
        # nextSmaller = getNextSmaller(heights,n)
        # print(prevSmaller)
        # print(nextSmaller)
        for idx in range(n):
            cur = heights[idx]
            t = nextSmaller[idx]
            s = prevSmaller[idx]
            L,R = max(0,idx-s)*cur,max(0,t-idx)*cur
            ans = max(ans,L+R-cur)
        return ans