class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        allCap = True
        allLower = True
        for i in word:
            if i.islower():
                allCap = False
            else:
                allLower = False
        if allCap or allLower:return True
        
        firstCap = word[0].isupper()
        for i in word[1:]:
            if i.isupper():
                return False
        return firstCap
            