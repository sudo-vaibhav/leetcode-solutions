# partial sum/ line-sweep approach
# from sortedcontainers import SortedDict
# class MyCalendarThree:

#     def __init__(self):
#         self.diff = SortedDict()

#     def book(self, start: int, end: int) -> int:
#         self.diff[start] = self.diff.get(start, 0) + 1
#         self.diff[end] = self.diff.get(end, 0) - 1
#         cur = res = 0
#         for delta in self.diff.values():
#             cur += delta
#             res = max(cur, res)
#         return res

# SegTree approach
class MyCalendarThree:
    def __init__(self):
        self.vals,self.lazy = Counter(),Counter()
    
    def update(self,start,end,left=0,right=10**9,idx=1):
        if start>right or end<left: return
        if start<=left <= right<=end:
            self.vals[idx]+=1
            self.lazy[idx]+=1
        else:
            m = (left+right)//2
            self.update(start,end,left,m,2*idx)
            self.update(start,end,m+1,right,2*idx+1)
            self.vals[idx] = self.lazy[idx]+max(self.vals[2*idx],self.vals[2*idx+1])
    def book(self,start,end):
        self.update(start,end-1)
        return self.vals[1]
        