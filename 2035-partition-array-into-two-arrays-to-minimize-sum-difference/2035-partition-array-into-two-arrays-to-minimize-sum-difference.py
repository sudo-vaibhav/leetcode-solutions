class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//2
        leftPart,rightPart = nums[:n],nums[n:]
        tot = sum(nums)
        totHalf = tot//2
        def getSums(arr):
            res = defaultdict(list)
            for size in range(1,n):
                for comb in combinations(arr,size):
                    res[size].append(sum(comb))
            return res
        
        
        leftSums,rightSums = getSums(leftPart),getSums(rightPart)
        
        ans = abs(sum(leftPart)-sum(rightPart))
        
        for takenFromLeft in range(1,n):
            
            takenFromRight = n - takenFromLeft
            
            lsums = leftSums[takenFromLeft]
            rsums = rightSums[takenFromRight]
            rsums.sort()
            
            for lsum in lsums:
                rest = totHalf - lsum
                
                idx = bisect_left(rsums,rest)
                
                for i in [idx,idx-1]:
                    if 0<=i<len(rsums):
                        curSum = lsum+rsums[i]
                        restSum = tot-curSum
                        ans = min(ans,abs(restSum-curSum))
        return ans