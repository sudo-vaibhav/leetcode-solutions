class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence=sentence.split()
        sentence.append(sentence[0])
        
        for i in range(1,len(sentence)):
            if sentence[i][0]!=sentence[i-1][-1]:
                return False
        return True