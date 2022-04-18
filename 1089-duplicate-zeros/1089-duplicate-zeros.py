class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zc = arr.count(0)
        n = len(arr)
        # print(zc)
        for i in range(n-1,-1,-1):
            cur = arr[i]
            # print(i,arr)
            if cur==0:
                zc-=1
                if i+zc<n:
                    arr[i+zc]=0
                    if i+zc<n-1:
                        arr[i+zc+1]=0
            else:
                newIdx = zc+i
                if newIdx<n:
                    arr[newIdx]=cur
        
        
        