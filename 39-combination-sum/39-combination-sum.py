class Solution:
    def solve(self,nums,target,so_far):
        if(target==0): self.ans.append(so_far)
        if(target>0):
            if(len(nums)>1):
                self.solve(nums[1:],target,so_far)
            self.solve(nums,target-nums[0],so_far+[nums[0]])
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans=[]
        self.solve(candidates,target,[])
        return self.ans