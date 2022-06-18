class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = list(map(set,["qwertyuiop","asdfghjkl","zxcvbnm"]))
        # print(rows)
        def check(word):
            w = set(word)
            
            for row in rows:
                temp = w.intersection(row) 
                # print(temp)
                if temp==w:
                    return True
            return False
        
        
        return [x for x in words if check(x.lower())]