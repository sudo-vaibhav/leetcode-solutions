class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # return len(set(arr))
        items = list(sorted(map(list,Counter(arr).items())))
        req = 1
        i = 0
        achieved = 0
        m = max(arr)
        # print(items,m)
        # req<m and 
        broken = False
        while i<len(items):
            # print(req,i,items[i])
            while i<len(items) and req>items[i][0]:
                i+=1
            
            if i>=len(items):
                broken = True
                break
            items[i][1] -= 1
            achieved = req
            req += 1
            if items[i][1] == 0:
                i+=1
        return achieved