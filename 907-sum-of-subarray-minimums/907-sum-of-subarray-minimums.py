class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        n = len(nums)
        nextSmaller = [n]*n
        prevSmaller = [-1]*n
        
         
        st = []
        
        
        for idx in range(n-1,-1,-1):
            while st and nums[st[-1]]>=nums[idx]:
                st.pop()
            if st:
                nextSmaller[idx] = st[-1]
            st.append(idx)
            
        st = []
        for idx in range(n):
            while st and nums[st[-1]]>nums[idx]:
                st.pop()
            if st:
                prevSmaller[idx] = st[-1]
            st.append(idx)
        
        print(nextSmaller,prevSmaller)
        ans,MOD = 0,10**9+7
        for i in range(n):
            cur = nums[i]
            ans  = (ans+cur*(nextSmaller[i]-i)*(i-prevSmaller[i]))%MOD
        
        return ans
            
            