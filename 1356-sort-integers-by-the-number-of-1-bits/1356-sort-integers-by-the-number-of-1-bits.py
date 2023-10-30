class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def b(x):
            ans = 0
            while x:
                ans+=1
                x&=(x-1)
            return ans
        return map(lambda x:x[1],sorted(map(lambda x:(b(x),x),arr)))