class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        ans = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                ans[i+j].append((j,nums[i][j]))
        res = []
        for i in sorted(ans.keys()):
            res.extend(map(lambda x:x[1],sorted(ans[i])))
        # print(ans)   
        return res