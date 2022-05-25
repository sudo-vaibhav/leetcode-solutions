class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        def lis(arr):
            res = []
            for _,v in arr:
                temp = bisect_left(res,v)
                if temp==len(res):
                    res.append(v)
                else:
                    res[temp]=v
            return len(res)
        
        return lis(envelopes)
        