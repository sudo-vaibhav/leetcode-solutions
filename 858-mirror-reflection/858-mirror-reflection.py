class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        b = q // gcd(p, q)
        a = b * p // q
        
        if a % 2 == 0:
            return 2

        return 0 if b % 2 == 0 else 1