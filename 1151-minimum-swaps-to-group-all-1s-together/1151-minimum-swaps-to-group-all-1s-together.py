class Solution:
    def minSwaps(self, data: List[int]) -> int:
        oneCount = data.count(1)
        n = len(data)
        ans = inf
        running = 0
        if oneCount==0: return 0
        for i in range(n):
            cur = data[i]
            running += cur==1
            if i>=oneCount-1:
                ans = min(ans,oneCount-running)
                running -= data[i-oneCount+1]==1
        return ans                