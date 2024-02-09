class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        n = len(nums)
        
        @cache
        def solve(i):
            # if i==n: return 1
            ans = 1
            for j in range(i+1,n):
                if nums[j]%nums[i]==0:
                    ans = max(ans,1+solve(j))
            return ans
        ans = 1
        for i in range(n):
            
            ans = max(ans,solve(i))
        # print(ans)
        
        looking = ans-1
        
        # last = n
        startfrom = -1
        
        for i in range(n):
            if solve(i)==ans:
                startfrom = i
                break
        res = [nums[startfrom]]
        last = startfrom
        while looking!=0:
            for j in range(last+1,n):
                if solve(j)==looking and nums[j]%nums[last]==0:
                    last = j
                    res.append(nums[j])
                    break        
            looking-=1
        return res
            