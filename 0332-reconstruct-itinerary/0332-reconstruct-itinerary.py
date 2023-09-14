class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = []
        adj = defaultdict(list)
        
        for s,e in tickets:
            heappush(adj[s],e)
        def solve(cur):
            while adj[cur]:
                dest = heappop(adj[cur])
                solve(dest)
            path.append(cur)
        solve("JFK")
        return path[::-1]