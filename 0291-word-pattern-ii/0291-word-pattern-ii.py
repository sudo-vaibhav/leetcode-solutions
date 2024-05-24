class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        
        def solve(i,j,mapping):
            if i==len(pattern) or j==len(s):
                return i==len(pattern) and j==len(s) 
            cur = pattern[i]
            if cur in mapping:
                if s[j:j+len(mapping[cur])] == mapping[cur]:
                    return solve(i+1,j+len(mapping[cur]),mapping)
                return False
            else:
                for k in range(j+1,len(s)+1):
                    m = s[j:k]
                    
                    
                    if m not in mapping.values():
                        mapping[cur]=m
                        if solve(i+1,k,mapping):
                            return True
                        del mapping[cur]
                return False
                
            
        return solve(0,0,{})