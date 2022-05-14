class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(lambda:defaultdict(int))
        
        for dep,dest in tickets:
            adj[dep][dest]+=1
            
        def solve(cur,path):
            path.append(cur)
            if len(path)==len(tickets)+1:
                return path
            else:
                for dest in sorted(adj[cur].keys()):
                    if adj[cur][dest]>0:
                        adj[cur][dest]-=1
                        temp = solve(dest,path)
                        if temp!=None:
                            return temp
                        adj[cur][dest]+=1
            path.pop()

            
        return solve("JFK",deque())
            
        