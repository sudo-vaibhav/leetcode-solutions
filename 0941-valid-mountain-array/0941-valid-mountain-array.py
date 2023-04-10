class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        n = len(arr)
        
        if n<3: return False
        tips = 0
        
        for i in range(n-1):
            if arr[i]==arr[i+1]:return False
        for i in range(1,n-1):
            if arr[i-1]<arr[i]>arr[i+1]:
                tips+=1
        if arr[0]>arr[1] or arr[-2]<arr[-1]: return False
        return tips==1