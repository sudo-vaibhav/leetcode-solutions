class Solution:
    def minOperations(self, s: str) -> int:
        
        
        def solve(initShouldBe):
            shouldBe = initShouldBe
            result = 0
            for c in s:
                if c==str(shouldBe):
                    pass
                else:
                    result+=1
                shouldBe = abs(1-shouldBe)
            return result
                    
        return min(solve(0),solve(1))