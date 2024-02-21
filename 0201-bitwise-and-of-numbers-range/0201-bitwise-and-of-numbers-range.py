class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifts=0
        while right!=left:
            left>>=1
            right>>=1
            shifts+=1
        return left<<shifts