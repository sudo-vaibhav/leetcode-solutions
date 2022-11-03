class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        d = defaultdict(int)
        
        for row in mat:
            for num in row:
                d[num]+=1
        
        for k in d:
            if d[k]==len(mat):
                return k
        
        return -1