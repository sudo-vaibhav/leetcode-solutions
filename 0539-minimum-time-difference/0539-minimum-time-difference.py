class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = []
        
        for tp in timePoints:
            h,m = map(int,tp.split(":"))
            arr.append(h*60+m)
        arr.sort()
        ans = inf
        for i in range(len(arr)-1):
            cur = arr[i]
            nex = arr[i+1]
            ans = min(ans,nex-cur)
        ans = min(ans,arr[0]+(24*60)-arr[-1])
        return ans
        