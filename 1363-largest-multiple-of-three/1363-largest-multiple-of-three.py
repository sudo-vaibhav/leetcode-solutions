class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        ans = ""
        ctr = Counter(digits)
        
        removeIfMod1 = [1,4,7,2,5,8]
        removeIfMod2 = [2,5,8,1,4,7]

        total = sum(digits)
        nums = range(9,-1,-1)
        
        while total%3!=0:
            toRemove = removeIfMod1 if total%3==1 else removeIfMod2
            
            for digit in toRemove:
                if ctr[digit]>0:
                    ctr[digit]-=1
                    total-=digit
                    break
        
        for num in nums:
            ans += str(num)*ctr[num]
        
        if len(ans)==0:
            return ""
        if ans[0]=="0":
            return "0"
        else:
            return ans