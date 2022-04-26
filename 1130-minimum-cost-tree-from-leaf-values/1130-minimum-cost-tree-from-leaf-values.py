class Solution:
    
            
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @cache
        def solve(l,r):
            if r<=l:return 0
            ans = inf
            for i in range(l,r):
                ans = min(ans,solve(l,i)+solve(i+1,r)+max(arr[l:i+1])*max(arr[i+1:r+1]))
            return ans

        n = len(arr)
        temp = solve(0,n-1)
        return temp