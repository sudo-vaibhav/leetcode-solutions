class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            i=0
            chunks = []
            while i<len(s):
                chunks.append(s[i:i+k])
                i+=k
            ans = ""
            for chunk in chunks:
                ans+=str(sum(map(int,chunk)))
            s = ans
        
        return s
            
                