class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return len(list(filter(lambda x:all(c in allowed for c in x),words)))