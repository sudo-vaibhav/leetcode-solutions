class Solution:
    def compressedString(self, word: str) -> str:
        i = 0
        ans = ""
        while i<len(word):
            j = 0
            while i+j<len(word) and word[i+j]==word[i] and j<9:
                j+=1
            ans += str(j)+word[i]
            # if j-i==9:
            #     i=j+1
            # else:
            i=i+j
        return ans