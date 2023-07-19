class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        def overlap(i1,i2):
            return i1[1]>i2[0] 
        # print(intervals)
        ans = 0
        prev = intervals[0]
        for i in range(1,len(intervals)):
            if overlap(prev,intervals[i]):
                ans+=1
                prev = prev if prev[1]<intervals[i][1] else intervals[i]
            else:
                prev = intervals[i]
            
        return ans