# from sortedcontainers import SortedList
# class Solution:
#     def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
#         m,n = len(mat),len(mat[0])
#         d = defaultdict(SortedList)
#         for i in range(m):
#             for j in range(n):
#                 """
#                 i-j is invariate across a diagonal, put
#                 all of its elements in sortedlist
#                 """
#                 d[i-j].add(mat[i][j]) 
#         for i in range(m):
#             for j in range(n):
#                 """
#                 starting from top left corner - we go in order for 
#                 each diagonal, and at each step give it the smallest element
#                 from the set and then pop that element from set since its 
#                 purpose is already fulfilled
#                 """
#                 mat[i][j] = d[i-j].pop(0)
#         return mat

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        minVal,maxVal = 1,100
        def sortDiag(startR,startC):
            nums = []
            r,c = startR,startC
            while r<m and c<n:
                nums.append(mat[r][c])
                r+=1
                c+=1
            ctr = Counter(nums)
            sortedNums = []
            for v in range(minVal,maxVal+1):
                sortedNums.extend([v]*ctr[v])
            
            r,c = startR,startC
            j = 0
            while r<m and c<n:
                mat[r][c] = sortedNums[j]
                j+=1
                r+=1
                c+=1
        
        for row in range(0,m):
            sortDiag(row,0)
        
        for col in range(1,n):
            sortDiag(0,col)
        
        return mat
        