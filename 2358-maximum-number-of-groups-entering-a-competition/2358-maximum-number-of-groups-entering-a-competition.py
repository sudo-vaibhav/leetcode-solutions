class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        # [10,6,12,7,3,5]
#         [3,5,6,7,10,12]
        n = len(grades)
        grades.sort()
        l,r= 0,0
        prev = 0
        prevSize = 0
        # running = 0
        ans = 0
        while r<n:
            running = 0
            while r<n and (running<=prev or r-l<=prevSize):
                running+=grades[r]
                r+=1
            # print(grades[l:r])
            if running>prev and r-l>prevSize:
                ans += 1
            prev = running
            prevSize = r-l
            l = r
        return ans