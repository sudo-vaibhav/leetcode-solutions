class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        arr = []
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                arr.append((nums[i][j],i))
        arr.sort()
        l = 0
        c = defaultdict(int)
        ans = [-inf,inf]
        for r in range(len(arr)):
            
            cur,arrIdx = arr[r]
            
            c[arrIdx]+=1
            
            while True:
                if len(c)==len(nums):
                    val,valArrIdx = arr[l]
                    if ans[1]-ans[0]>cur-val:
                        ans = [val,cur]
                    c[valArrIdx]-=1
                    if c[valArrIdx]==0:
                        del c[valArrIdx]
                    l+=1
                else:
                    break
        return ans
                
            