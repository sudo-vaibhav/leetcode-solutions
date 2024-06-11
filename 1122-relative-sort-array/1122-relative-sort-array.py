class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {v:i for i,v in enumerate(arr2)}
        res = []
        for i in arr1:
            if i in d:
                res.append(i)
        res.sort(key=lambda x:d[x])
        res2 = []
        for i in arr1:
            if i not in d:
                res2.append(i)
        res2.sort()
        return [*res,*res2]