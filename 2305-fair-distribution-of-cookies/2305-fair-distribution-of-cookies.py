class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        dist = [0]*k
        ans = inf
        
        n = len(cookies)
        
        
        # @cache
        def solve(i,childleft):
            # dist = list(dist)
            # nonlocal ans
            leftjars = n-i
            if leftjars<childleft: return inf
            if i==n:
                return max(dist)
                # print(dist)
                # ans = min(ans,max(dist))
            else:
                ans = inf
                for j in range(k):
                    childleft -= dist[j]==0
                    dist[j]+=cookies[i]
                    ans = min(ans,solve(i+1,childleft))
                    # dist
                    dist[j]-=cookies[i]
                    childleft += dist[j]==0
                    # solve(i+1,tuple(dist))
                return ans
        return solve(0,k)
        
        # return ans