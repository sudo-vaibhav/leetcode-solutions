class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        target = inf
        for i in range(n-1):
            target = min(target,arr[i+1]-arr[i])
        ans = []
        for i in range(n-1):
            if arr[i+1]-arr[i]==target:
                ans.append([arr[i],arr[i+1]])
        return ans