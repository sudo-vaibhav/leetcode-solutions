class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # building = defaultdict(lambda :[0,0])
        m = len(requests)
        taken = []
        def solve(i):
            if i==m:
                check = defaultdict(int)
                for fro,to in taken:
                    check[fro]+=1
                    check[to]-=1
                return len(taken) if all(map(lambda x:x==0,check.values())) else 0 
                # return sum(map(lambda x:min(x),building.values()))
            # fro,to = requests[i] 
            ans = solve(i+1)
            # building[fro][0]+=1
            # building[to][1]+=1
            taken.append(requests[i])
            ans = max(ans,solve(i+1))
            taken.pop()
            # solve(i+1)
            # building[fro][0]-=1
            # building[to][1]-=1
            return ans
        
        return solve(0)
            