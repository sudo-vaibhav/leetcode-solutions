class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        st = []
        vis = set()
        
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
        
        # gvis = set()
        
        def toposort(i):
            vis.add(i)
            # gvis.add(i)
            for dest in adj[i]:
                if dest not in vis:
                    toposort(dest)
            # vis.remove(i)
            
            
            st.append(i)
        
        for i in range(n):
            if i not in vis:
                toposort(i)
                
        f = st[::-1]
        # print(st)
        st = []
        vis = set()
        ans = []
        for i in f:
            if i not in vis:
                ans.append(i)
                toposort(i)
        return ans