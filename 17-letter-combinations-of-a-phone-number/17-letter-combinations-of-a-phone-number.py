class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        n = len(digits)
        
        if n == 0 : return [] 
        
        def solve(i,digits,prev):
            if(i==n): return prev
            ans = []
            for s in prev:
                for letter in letters[digits[i]]:
                    ans.append(s+letter)
            
            return solve(i+1,digits,ans)
            
        return solve(0,digits,[""])