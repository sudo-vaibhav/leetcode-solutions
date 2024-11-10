class Solution:
    
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)
        n = len(nums)
        l = 0
        def getNum(d):
            ans = 0
            for i in d:
                if d[i]>0:
                    ans |= 1<<i
            return ans
        # running = 
        ans = inf
        for r in range(n):
            # running |= nums[r]
            temp = bin(nums[r])[2:][::-1]
            for i in range(len(temp)):
                if temp[i]=="1":
                    c[i]+=1
            
            while l<=r and getNum(c)>=k:
                ans = min(ans,r-l+1)
                
                temp2 = bin(nums[l])[2:][::-1]
                for j in range(len(temp2)):
                    if temp2[j]=='1':
                        c[j]-=1
                l+=1
        return ans if ans!=inf else -1