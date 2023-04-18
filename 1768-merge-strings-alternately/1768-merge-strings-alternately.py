class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m= min(map(len,[word1,word2]))
        return "".join(map("".join,zip(word1,word2)))+word1[m:]+word2[m:]