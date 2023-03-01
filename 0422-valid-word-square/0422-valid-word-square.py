class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        m,n = len(words),max(map(len,words))
        k = max(m,n)
        for i in range(k):
            for j in range(k):
                w1,w2 = "  "
                try:
                    w1 = words[i][j]
                except:pass
                try:
                    w2 = words[j][i]
                except:pass
                # if max(i,j)<=
                if w1!=w2:
                    return False
        return True