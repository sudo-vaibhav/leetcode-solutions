class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        path = deque()
        
        for dep,dest in tickets:
            heappush(adj[dep],dest)
            
        def solve(cur):            
            while adj[cur]:
                dest = heappop(adj[cur])
                solve(dest)
            path.appendleft(cur)

            
        solve("JFK")
        
        return path