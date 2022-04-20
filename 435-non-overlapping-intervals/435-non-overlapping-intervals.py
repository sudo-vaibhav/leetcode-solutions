class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         minimum overlapping intervals to remove is equivalent to
#         n - maximum non overlapping intervals possible
        cnt,n = 1,len(intervals)
        intervals.sort(key=lambda x: x[1])
        prev = intervals[0]
        for i in range(1,n):
            cur = intervals[i]
            if cur[0]>=prev[1]:
                cnt+=1
                prev = prev if prev[1]>cur[1] else cur
        return n-cnt
                
            
    