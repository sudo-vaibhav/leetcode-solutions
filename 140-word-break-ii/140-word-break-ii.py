class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        words = set(wordDict)
        n = len(s)
        def solve(i,path):
            if i==n:
                ans.append(" ".join(path))
            else:
                cur = ""
                for end in range(i,n):
                    cur += s[end]
                    if cur in words:
                        path.append(cur)
                        solve(end+1,path)
                        path.pop()
            
        solve(0,[])
        return ans