class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ans = 0
        visited = set()
        
        def dfs(city):
            for idx,neigh in enumerate(isConnected[city]):
                if neigh and idx not in visited:
                    visited.add(idx)
                    dfs(idx)
            
        for city in range(0,n):
            if city not in visited:
                ans+=1
                visited.add(city)
                dfs(city)
        return ans