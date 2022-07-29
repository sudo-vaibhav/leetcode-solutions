class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        base = 26
        MOD = 2**63-1
#         def getAlloc(s):
#             n = len(s)
#             ans = []
#             alloc = {}
#             c = 0
#             for i in s:
#                 if i in alloc:
#                     pass
#                 else:
#                     alloc[i]=c
#                     c+=1
#                 ans.append(alloc[i])
#             return ans
        
#         main = getAlloc(pattern)
#         res = []
#         for w in words:
#             if getAlloc(w)==main:
#                 res.append(w)
        
#         return res
        def getAlloc(s):
            n = len(s)
            ans = 0
            alloc = {}
            c = 0
            for i in s:
                ans = (ans*base)%MOD
                if i in alloc:
                    pass
                else:
                    alloc[i]=c
                    c+=1

                ans = (ans+alloc[i])%MOD
            return ans

        main = getAlloc(pattern)
#         for w in words:
            
        res = []
        for w in words:
            if getAlloc(w)==main:
                res.append(w)

        return res