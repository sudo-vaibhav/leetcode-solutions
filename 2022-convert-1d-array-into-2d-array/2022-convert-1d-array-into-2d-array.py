class Solution:
    def construct2DArray(self, orig: List[int], m: int, n: int) -> List[List[int]]:
        temp = len(orig)
        
        if temp!=m*n:
            return []
        
        arr = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                arr[i][j] = orig[i*n+j]
        return arr