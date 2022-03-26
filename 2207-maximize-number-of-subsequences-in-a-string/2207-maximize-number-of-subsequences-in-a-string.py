class Solution:
    def f1(self,text,c):
        m=0
        # print(c)
        nums = [0 for _ in range(len(text))]
        for i in range(len(text)-1,-1,-1):
            if text[i]==c:
                m+=1
                nums[i]=m
            else:
                nums[i]=m
        # print(nums)
        return nums
              
    def f2(self,text,compleCount,c,comple):
        ans=0
        for i in range(len(text)):
            if text[i]==c:
                if comple==c:
                    ans+= compleCount[i]-1
                else:
                    ans+=compleCount[i]
        return ans
                    
        
                
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        c1,c2 = list(pattern)        
        o1, o2 = c1+text,text+c2
        
        t1 = self.f1(o1,c2)
        t2 = self.f1(o2,c2)
        
        return max(self.f2(o1,t1,c1,c2),self.f2(o2,t2,c1,c2))
        
        
        