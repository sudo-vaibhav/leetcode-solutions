class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum([i for i in nums if i%2==0])
        ans = []
        for v,idx in queries:
            old = nums[idx]
            if old%2==0:
                s -= old
            if (v+old)%2==0:
                s += v+old
            nums[idx]=v+old
            ans.append(s)
            
        return ans