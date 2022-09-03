class Solution:
    def numsSameConsecDiff(self, N: int, k: int) -> List[int]:
        ans = []
        
        def solve(n,prev,path):
            if n==0:
                ans.append("".join(map(str,path)))
            else:
                for num in range(0,10):
                    if num==0 and n==N:
                        continue
                    if n==N or abs(prev-num)==k:
                        path.append(num)
                        solve(n-1,num,path)
                        path.pop()
        
        solve(N,0,[])
        
        return ans