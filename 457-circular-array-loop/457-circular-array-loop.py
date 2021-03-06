class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def checkCyc(i,pos):
            slow,fast = i,i
            while True:
                if (nums[fast]>0) ^ pos:
                    return False
                newSlow = nums[slow]+slow
                newFast = nums[fast]+fast
                slow = newSlow%n 
                fast = newFast%n
                if (nums[fast]>0) ^ pos:
                    return False
                newFast = nums[fast]+fast
                fast = newFast%n
                if (fast==slow):
                    break
            return (slow+nums[slow])%n!=slow
            
        for i in range(n):
            if checkCyc(i,nums[i]>0):
                return True
        return False
            
            