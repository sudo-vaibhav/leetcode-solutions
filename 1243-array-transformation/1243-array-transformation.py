class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            ans = list(arr)
            i = 1
            while i<len(arr)-1:
                prev,nex = arr[i-1],arr[i+1]
                cur = arr[i]
                if cur<prev and cur<nex:
                    ans[i]+=1
                elif cur>prev and cur>nex:
                    ans[i]-=1
                i+=1
            if ans==arr:
                break
            else:
                arr = ans                
        return ans