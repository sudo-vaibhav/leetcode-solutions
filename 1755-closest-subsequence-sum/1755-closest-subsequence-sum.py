class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)//2
        leftPart,rightPart = nums[:n],nums[n:]
        # tot = sum(nums)
        # totHalf = tot//2
        def getSums(arr):
            res = defaultdict(list)
            n = len(arr)
            res =[0]
            for size in range(1,n+1):
                for comb in combinations(arr,size):
                    res.append(sum(comb))
            return res
        lsums,rsums = getSums(leftPart),getSums(rightPart)
        rsums.sort()
        ans = abs(goal)
        # for t in range(0,n+1):
        for lsum in lsums:
            # for takenFromRight in range(0,n+1):
            #     rsums = rightSums[takenFromRight]
            #     for lsum in lsums:
            rest = goal - lsum
            idx = bisect_left(rsums,rest)
            for i in [idx,idx-1]:
                if 0<=i<len(rsums):
                    curSum = lsum+rsums[i]
                    ans = min(ans,abs(goal-curSum))
        return ans
        