class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        
        hash_base = 29
        MOD = 10**9+7
        forward,reverse = 0,0
        longest_palin = 1
        power = 0
        for i,v in enumerate(s):
            temp = ord(v)-ord("a")+1
            forward = (forward*hash_base+(temp))%MOD
            reverse = ((pow(hash_base,power,MOD))*temp + reverse)%MOD
            power += 1
            if forward==reverse:
                longest_palin = i+1
        return s[longest_palin:][::-1]+s
        
        
#         aacecaaa
#         aaacecaa
        
        