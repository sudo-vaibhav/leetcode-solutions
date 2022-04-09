class Solution:
    def sumOfThree(self, n: int) -> List[int]:
#         k-1, k , k+1
#  3k = n
# 
        if n%3!=0: return []
        else:
            f = n//3
            return [f-1,f,f+1]