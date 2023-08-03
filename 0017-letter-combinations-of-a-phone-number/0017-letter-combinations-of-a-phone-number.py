class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        n = len(digits)
        
        mapping = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        def solve(soFar,idx):
            if idx==n:
                ans.append(soFar)
            else:
                cur = digits[idx]
                for char in mapping[cur]:
                    solve(soFar+char,idx+1)
        if n==0: return []      
        solve("",0)
            
        return ans