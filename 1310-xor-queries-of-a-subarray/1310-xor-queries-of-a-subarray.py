class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        p = [0]
        
        for r in arr:
            p.append(p[-1]^r)
        ans = []
        for i,j in queries:
            ans.append(p[j+1]^p[i])
        return ans