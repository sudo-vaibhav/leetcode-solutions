class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        date,cnt = 0,0
        courses.sort(key=lambda x:x[1])
        runningTime = 0
        heap = []
        for duration,lastDay in courses:
            runningTime += duration
            heappush(heap,-duration)
            if runningTime>lastDay:
                longestPreviouslyDoneTime = -heappop(heap)
                runningTime -= longestPreviouslyDoneTime
        return len(heap)