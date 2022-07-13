class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        root = None
        n = len(pid)
        
        adj = defaultdict(list)
        
        for i in range(n):
            cur = pid[i]
            par = ppid[i]
            if par == 0:
                root = cur
            else:
                adj[par].append(cur)
        
        def lvr(node):
            ans = [node]
            for child in adj[node]:
                ans.extend(lvr(child))
            return ans
        def solve(node):
            if node==kill:
                return lvr(node)
            else:
                ans = []
                for child in adj[node]:
                    ans.extend(solve(child))
                return ans
            
        return solve(root)