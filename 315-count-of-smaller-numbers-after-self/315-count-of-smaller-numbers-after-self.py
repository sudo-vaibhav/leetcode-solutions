class Solution:
#     let binary index tree store cumulative frequency of numbers in different ranges
    def initTree(self,nums):
        n = 2*(10**4)+1
        self.ftree = [0]*(n+1)
        
    def update(self,idx,val):
        idx+=1
        while idx<len(self.ftree):
            self.ftree[idx]+=val
            idx+=idx&(-idx)
        
    def getSum(self,idx):
        s=0
        idx+=1
        while idx>0:
            s+=self.ftree[idx]
            idx-=idx&(-idx)
        return s
            
    def countSmaller(self, nums: List[int]) -> List[int]:
        revnums = [1+x+(10**4) for x in nums[::-1]]
        ans = []
        self.initTree(revnums)
        
        for idx,n in enumerate(revnums):
            ans.append(self.getSum(n-1))
            self.update(n,1)
        return ans[::-1]
        