class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        arr = []
        
        
        def solve(i):
            if i==n+1:
                if len(arr)==k:
                    ans.append(list(arr))
            else:
                solve(i+1)
                arr.append(i)
                solve(i+1)
                arr.pop()
        
        solve(1)
        
        return ans
                