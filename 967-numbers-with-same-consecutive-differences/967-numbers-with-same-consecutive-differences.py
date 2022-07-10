class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        ans = []
        
        N = n
        def solve(n,prev):
            if n==0:
                ans.append(int(''.join(map(str,prev))))
                return 
            else:
                for cur in range(0,10):
                    if cur==0 and n==N:
                        continue
                    if (n==N) or (n!=N and abs(cur-prev[-1])==k):
#                         can pick cur
                        prev.append(cur)
                        solve(n-1,prev)
                        prev.pop()
        
        solve(n,[])
        return ans