class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        S,P = len(s),len(p)
        
        @cache
        def matches(i,j):
            if j>=P:
                return i==S and j==P
            else:
                if p[j]=="?":
                    return matches(i+1,j+1) 
                elif p[j]=="*":
                    for I in range(i,S+1):
                        if matches(I,j+1):
                            return True
                else:
                    return i<S and s[i]==p[j] and matches(i+1,j+1)
            return False
            
        return matches(0,0)