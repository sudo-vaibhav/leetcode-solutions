class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowelMap = {"a":1<<0,"e":1<<1,"i":1<<2,"o":1<<3,"u":1<<4}
        allowMap = {vowelMap[key]:reduce(lambda x,y:x|y,map(lambda x:vowelMap[x],val)) for key,val in ({"a":"e","e":"ai","i":"aeou","o":"iu","u":"a"}).items()}
        
        # print(allowMap)
        MOD = (10**9)+7
        @cache
        def solve(i=0,allowed=((1<<5)-1)):
            # print(bin(allowed))
            if i==n:return 1
            ans = 0
            for c in "aeiou":
                mask = vowelMap[c]
                if mask&allowed:
                    ans = (ans+solve(i+1,allowMap[mask]))%MOD
            
            return ans
        return solve()