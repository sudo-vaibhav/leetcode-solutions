class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        
        s = deque(str1)
        def nex(c):
            if c=="z":
                return "a"
            return chr(ord(c)+1)
        for i in str2:
            while s and not (s[0]==i or nex(s[0])==i):
                s.popleft()
            if not s:
                return False
            s.popleft()
        return True