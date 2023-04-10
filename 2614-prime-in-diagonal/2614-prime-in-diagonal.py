# import sympy
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        
        diags = []
        
        for i in range(n):
            # for j in range(n):
                diags.append(nums[i][i])
                diags.append(nums[i][n-i-1])
        
        ans = 0
        
        for num in filter(lambda x:x!=1,diags):
            if num==2:
                ans = max(ans,2)
            else:
                for i in range(2,ceil(num**0.5)+1):
                    if num%i==0:
                        break
                else:
                    ans = max(ans,num)
        return ans