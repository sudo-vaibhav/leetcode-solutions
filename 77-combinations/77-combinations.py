class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,n+1))
        ans = []
        
        def solve(idx,k,picks):
            if idx==n:
                if k==0:
                    ans.append(list(picks))
            else:
                numsLeft = n-idx
                
                picks.append(nums[idx])
                solve(idx+1,k-1,picks)
                picks.pop()
                
#                 sometimes we can ignore inserting
                if k<numsLeft:
                    solve(idx+1,k,picks)
                
                
        
        solve(0,k,deque())
        
        return ans