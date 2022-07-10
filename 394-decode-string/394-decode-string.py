class Solution:
    def decodeString(self, s: str) -> str:
        
        
        
        
        i = 0
        j = len(s)
        
        def solve():
            nonlocal i,j
            mydig = ""
            while i<j and s[i].isdigit():
                mydig += s[i]
                i+=1
            if not mydig:
                i+=1
                
                return s[i-1] 
            mydig = int(mydig)
            ans = ""
            i+=1
            while i<j and s[i]!="]":
                if s[i].isdigit():
                    ans += solve()
                else:
                    ans += s[i]
                    i+=1
            i+=1
            ans = ans * mydig
            return ans
        
        res = ""
        while i<j:
            res += solve()
        return res