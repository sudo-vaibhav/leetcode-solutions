class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note,mz = Counter(ransomNote),Counter(magazine)
        
        for c in note:
            if note[c]>mz[c]:return False
        return True
        