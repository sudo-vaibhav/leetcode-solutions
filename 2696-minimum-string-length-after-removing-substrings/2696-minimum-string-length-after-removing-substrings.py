class Solution:
    def minLength(self, s: str) -> int:
        prevLen = inf
        
        while prevLen!=len(s):
            prevLen = len(s)
            s = s.replace("AB","").replace("CD","")
            
        return len(s)
        