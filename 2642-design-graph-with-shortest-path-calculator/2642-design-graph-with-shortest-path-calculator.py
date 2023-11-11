class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = defaultdict(list)
        self.n = n
        for edge in edges:
            self.adj[edge[0]].append(edge[1:])
        
    def addEdge(self, edge: List[int]) -> None:
        self.adj[edge[0]].append(edge[1:])

    def shortestPath(self, node1: int, node2: int) -> int:
        hp = [(node1,0)]
        dists = [inf]*self.n
        dists[node1]=0
        
        while hp:
            node,dist = heappop(hp)
            if dist>dists[node]:
                continue
            for v,w in self.adj[node]:
                if dist+w<dists[v]:
                    dists[v]=dist+w
                    heappush(hp,(v,dists[v]))
        return dists[node2] if dists[node2]!=inf else -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)