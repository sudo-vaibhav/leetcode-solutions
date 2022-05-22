class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = list(pattern)
        s = s.split()
        mapping = {}
        mapping2 = {}
        if len(s)!=len(p):
            return False
        for idx,v in enumerate(s):
            if p[idx] not in mapping and v not in mapping2:
                mapping[p[idx]] = v
                mapping2[v] = p[idx]
            elif p[idx] in mapping and v in mapping2:
                if mapping[p[idx]]!=v or mapping2[v]!=p[idx]:
                    return False
            else:
                return False
        return True