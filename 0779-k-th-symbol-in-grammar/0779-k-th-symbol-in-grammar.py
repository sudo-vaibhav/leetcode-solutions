class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 1->0
        # 2->01
        # 3->0110
        # 4->0110 1001
        # 5->01101001 10010110
        # 6->0110100110010110 1001011001101001
        # n=5
        prev = 0
        level=1
        for level in range(2,n+1):
            shiftAmt = 2**(level-2)
            newRight = ((1<<shiftAmt)-1)^prev
            prev = (prev<<shiftAmt)|newRight
        return (prev>>((2**(level-1))-k))&1