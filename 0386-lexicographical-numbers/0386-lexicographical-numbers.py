class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def solve(prev):
            
            for i in range(0,10):
                newNum = prev+str(i)
                num = int(newNum)
                if num<=n and num>0:
                    ans.append(newNum)
                    solve(newNum)
        solve("")
        return map(int,ans)