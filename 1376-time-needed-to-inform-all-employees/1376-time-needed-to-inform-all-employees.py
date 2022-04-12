class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for i in range(n)]
        
        for idx,par in enumerate(manager):
            if par>=0:
                children[par].append(idx)
                
        # print(children)
        def dfs(node):
            return informTime[node]+(max([dfs(child) for child in children[node]])if children[node] else 0)
                
        return dfs(headID)