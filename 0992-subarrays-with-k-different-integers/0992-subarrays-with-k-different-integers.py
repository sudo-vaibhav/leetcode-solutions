class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # l,L = 0,0
        
        def findDistinctStart(k):
            l = 0
            c = defaultdict(int)
            ans = []
            for r in range(n):
                c[nums[r]]+=1
                while len(c)>k:
                    c[nums[l]]-=1
                    if c[nums[l]]==0:
                        del c[nums[l]]
                    l+=1
                ans.append(l)
            return ans
#         for r in range(n):
#             c[nums[r]]+=1
#             if len(c)>k:
                
#                 removals = defaultdict(int)
                
#                 while removals[nums[l]]
        
        a1 = findDistinctStart(k)
        a2 = findDistinctStart(k-1)
        ans = 0
        for i in range(n):
            ans += a2[i]-a1[i]
        return ans