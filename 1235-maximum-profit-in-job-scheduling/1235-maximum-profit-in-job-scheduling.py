class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = list(zip(startTime,endTime,profit))
        arr.sort()
        n = len(arr)
        @cache
        def solve(i):
            if i>=n:
                return 0
            ans = solve(i+1)
            s,e,p = arr[i]
            # print(s,e,p)
            temp = p+solve(bisect_left(arr,(e,)))
            # print(temp)
            ans = max(ans,temp)
            return ans
        
        return solve(0)