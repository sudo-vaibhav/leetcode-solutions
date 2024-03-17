class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        S,E = newInterval
        ans = []
        a,b=S,E
        while i <(len(intervals)):
            s,e = intervals[i]
            if e<a:
                ans.append((s,e))
            elif s>b:
                break
            else:
                a = min(a,s)
                b = max(b,e)
            i+=1
                
        ans.append((a,b))
        while i<len(intervals):
            ans.append(intervals[i])
            i+=1
        return ans