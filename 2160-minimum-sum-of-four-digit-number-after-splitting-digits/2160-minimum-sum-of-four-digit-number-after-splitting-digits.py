
class Solution:
    def minimumSum(self, x: int) -> int:
        digits=list(str(x))
        print(digits)
        ans = 10000
        for permutation in permutations(digits):
            x = int("".join(permutation))
            print(x)
            ans = min(ans,min(map(lambda x: x[0]+x[1], [ [x%i,(x-x%i)/i] for i in [100,10]] )))
        return int(ans)