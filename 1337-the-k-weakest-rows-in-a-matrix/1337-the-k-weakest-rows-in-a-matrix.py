class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        s = []
        for idx,row in enumerate(mat):
            s.append((row.count(1),idx))
        
        s=sorted(s)
        ans = []
        for j in s[:k]:
            ans.append(j[1])
        return ans
        
        