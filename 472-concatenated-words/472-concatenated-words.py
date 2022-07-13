class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        
        present = set()
        
        def check(word):
            def solve(i):
                if i>=len(word):
                    return True
                cur = ""
                for end in range(i,len(word)):
                    cur += word[end]
                    if cur in present and solve(end+1):
                        return True
                
                return False
            return solve(0)
                        
        
        
        words.sort(key=lambda x:len(x))
        ans = []
        for word in words:
            # print(word)
            if check(word):
                ans.append(word)
            
            present.add(word)
        
        return ans