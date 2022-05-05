class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = []
        prev = intervals[0]
        for interval in intervals[1:]:
            start,end = interval
            if start>prev[1]:
                ans.append(prev)
                prev = interval
            else:
                prev = [min(prev[0],start),max(prev[1],end)]
        ans.append(prev)
        return ans