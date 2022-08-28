from sortedcontainers import SortedList
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        d = defaultdict(SortedList)
        
        for i in range(m):
            for j in range(n):
                d[i-j].add(mat[i][j])
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i-j].pop(0)
        return mat