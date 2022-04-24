class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        n = len(s)
        def solve(idx,string):
            if idx==n:
                res.append("".join(string))
            else:
                if string[idx].isalpha():
                    orig = string[idx]
                    
                    if string[idx].islower():
                        string[idx] = string[idx].upper()
                    else:
                        string[idx] = string[idx].lower()
                    solve(idx+1,string)
                    string[idx] = orig                    
                solve(idx+1,string)                    
        
        solve(0,list(s))
        return res