class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def solve(cur=1,k=k,s=0,path=[]):
            if k==0 or cur>9:
                if s==n and k==0:
                    ans.append(list(path))
            else:
                solve(cur+1,k,s,path)
                path.append(cur)
                solve(cur+1,k-1,s+cur,path)
                path.pop()

        solve()
        return ans

