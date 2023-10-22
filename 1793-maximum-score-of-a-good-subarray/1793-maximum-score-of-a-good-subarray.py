class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = []
        prevSmaller = [-1]*n
        nextSmaller = [n]*n
        
        for i in range(n):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            if st:
                prevSmaller[i]=st[-1]
            st.append(i)
        st = []
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            if st:
                nextSmaller[i]=st[-1]
            st.append(i)
        ans= 0
        # print(nums)
        for i in range(n):
            val = nums[i]
            prev,nex = prevSmaller[i]+1,nextSmaller[i]-1
            # print(prev,k,nex)
            if prev<=k<=nex:
                
                items = nex-prev+1
                ans = max(ans,items*val)
        
        return ans