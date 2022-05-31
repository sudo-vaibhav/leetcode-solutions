#User function Template for python3

class Solution:
    def findPath(self, m, n):
        free,blocked = 1,0
        ans = []
        moves = [0,-1,0,1,0]
        vis = [[False for _ in range(n)] for _ in range(n)]
        mapping = {
            (0,1):"R",
            (0,-1):"L",
            (-1,0):"U",
            (1,0):"D"
        }
        
        def dfs(i,j,path):
            if 0>i or 0>j or n-1<j or n-1<i or vis[i][j] or m[i][j]==blocked: return 
            vis[i][j]=True
            if i==n-1 and j==n-1:
                ans.append(str(path))
            else:
                for di,dj in zip(moves[1:],moves[:-1]):
                    I,J = i+di,j+dj
                    dfs(I,J,path+mapping[(di,dj)])
            vis[i][j]=False
            
        
        dfs(0,0,"")
        return ans
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends