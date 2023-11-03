class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        def solve(i,cur):
            if cur==n+1 or i==len(target):
                return
            if target[i]==cur:
                ans.append("Push")
                solve(i+1,cur+1)
            else:
                ans.append("Push")
                ans.append("Pop")
                solve(i,cur+1)
        solve(0,1)
        return ans