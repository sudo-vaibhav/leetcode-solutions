class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals)<=1: return True
        intervals.sort()
        prev = intervals[0]
        for meet in intervals[1:]:
            if meet[0]>=prev[1]:
                prev = meet
            else:
                return False
                
        return True