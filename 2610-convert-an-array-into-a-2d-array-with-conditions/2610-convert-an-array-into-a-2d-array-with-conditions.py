class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ct = Counter(nums)
        
        ans = []
        
        while ct.keys():
            temp = []
            keys = list(ct.keys())
            for k in keys:
                temp.append(k)
                ct[k]-=1
                if ct[k]==0: del ct[k]
            ans.append(temp)
        
        return ans