#User function Template for python3
from collections import defaultdict

#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(adjMat, m, n):
    color = [0 for _ in range(n)]
    def isSafe(node,col):
        for dest in range(n):
            if adjMat[node][dest]==1:
                if color[dest]==col:return False
        return True
    def canAssign(node):
        if node==n:return True
        for col in range(1,m+1):
            if isSafe(node,col):
                color[node]=col
                if canAssign(node+1):
                    return True
                color[node]=0
        return False
    return 1 if canAssign(0) else 0
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends