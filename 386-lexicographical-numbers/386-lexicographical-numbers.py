class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [str(i) for i in range(1,n+1)]
        
        nums.sort()
        
        return [int(i) for i in nums]