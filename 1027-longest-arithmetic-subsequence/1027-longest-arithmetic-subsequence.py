class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 2
        
# solve function returns the max possible length ap starting from given index        
        dp = [defaultdict(lambda:1) for _ in range(n)]
        
        for end in range(n):
            for start in range(end):
                diff = nums[end]-nums[start]
                dp[end][diff] = max(dp[end][diff],1+dp[start][diff])
                
    
#         @cache
#         def solve(startIdx,d):
#             if startIdx==n-1:
#                 return 1
#             tmpans = 1
#             for nextIdx in range(startIdx+1,n):
#                 if nums[nextIdx]-nums[startIdx]==d:
#                     temp = 1+solve(nextIdx,d)
#                     tmpans = max(tmpans,temp)
#             return tmpans
        return max(max(i.values()) for i in dp)
        
        
#         n^2
        # for start in range(n-1):
        #     for nex in range(start+1,n):
        #         ans = max(ans,solve(start,nums[nex]-nums[start]))
        
#         m = defaultdict(int)
#         for start in range(n):
#             for nex in range(start+1,n):
#                 m[nums[nex]-nums[start]]+=1
                
        # return ans