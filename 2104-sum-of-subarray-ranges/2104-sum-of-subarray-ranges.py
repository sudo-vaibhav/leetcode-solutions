class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
#         ans = 0
#         n = len(nums)
#         for start in range(n):
#             mini,maxi = nums[start],nums[start]
#             for end in range(start,n):
#                 maxi = max(maxi,nums[end])
#                 mini = min(mini,nums[end])
#                 ans += maxi-mini
#         return ans


        st = []
        n = len(nums)
        nextGreater = [n]*n
        nextSmaller = [n]*n
        prevSmaller = [-1]*n
        prevGreater = [-1]*n
        
        for idx in range(n-1,-1,-1):
            while st and nums[st[-1]]>=nums[idx]:
                st.pop()
            if st:
                nextSmaller[idx] = st[-1]
            st.append(idx)
        
        st = []
        
        
        for idx in range(n-1,-1,-1):
            while st and nums[st[-1]]<=nums[idx]:
                st.pop()
            if st:
                nextGreater[idx] = st[-1]
            st.append(idx)
        st = []
        for idx in range(n):
            while st and nums[st[-1]]<nums[idx]:
                st.pop()
            if st:
                prevGreater[idx] = st[-1]
            st.append(idx)
        
        st = []
        for idx in range(n):
            while st and nums[st[-1]]>nums[idx]:
                st.pop()
            if st:
                prevSmaller[idx] = st[-1]
            st.append(idx)
        
        ans = 0
        # print(nextGreater,prevGreater,nextSmaller,prevSmaller)
        for i in range(n):
            cur = nums[i]
            plus,minus = (i-prevGreater[i])*(nextGreater[i]-i),(i-prevSmaller[i])*(nextSmaller[i]-i)
            ans += plus*cur
            ans -= minus*cur
            # print(plus,minus,i)
        
        return ans
        