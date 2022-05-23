class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = ["" for _ in range(10)]
        
        for w in s.split():
            word = w[:-1]
            pos = int(w[-1])
            words[pos] = word
            
        ans = []
        
        for w in words:
            if w!="":
                ans.append(w)
        
        return " ".join(ans)