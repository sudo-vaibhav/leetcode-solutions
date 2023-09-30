class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<3: return False
        prevG = [-1]*n
        st = []
        for idx,num in enumerate(nums):
            while st and st[-1][0]<=num:
                st.pop()
            if st:
                prevG[idx]=st[-1][1]
            st.append((num,idx))
        def prevGreater(i):
            return prevG[i]
        @cache
        def minTill(i):
            if i<0: return inf
            if i==0: return nums[0]
            return min(nums[i],minTill(i-1))
        
        for i in range(2,n):
            idx = prevGreater(i)
            if idx<0: continue
            smallest = minTill(idx-1)
            if smallest<nums[i]<nums[idx]: return True
            # print("valid ans",smallest,nums[i],nums[idx])
            # return True
        return False