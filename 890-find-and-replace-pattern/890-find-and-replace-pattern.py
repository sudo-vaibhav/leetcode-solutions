class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def getAlloc(s):
            n = len(s)
            ans = []
            alloc = {}
            c = 0
            for i in s:
                if i in alloc:
                    pass
                else:
                    alloc[i]=c
                    c+=1
                ans.append(alloc[i])
            return ans
        
        main = getAlloc(pattern)
        res = []
        for w in words:
            if getAlloc(w)==main:
                res.append(w)
        
        return res