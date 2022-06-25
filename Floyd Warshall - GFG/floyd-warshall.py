#User function template for Python
from math import inf
class Solution:
	def shortest_distance(self, mat):
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if mat[i][j]==-1:
                    mat[i][j] = inf
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][k]+mat[k][j],mat[i][j])
        
        for i in range(n):
            for j in range(n):
                if mat[i][j]==inf:
                    mat[i][j] = -1
#{ 
#  Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends