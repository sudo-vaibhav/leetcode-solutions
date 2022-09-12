class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        score = 0
        taken = []
        
        l,r = 0,n-1
        while l<=r:
            if power>=tokens[l]:
                score+=1
                power-=tokens[l]
                l+=1
            elif score>0:
                if l!=r:
                    score-=1
                    power+=tokens[r]
                    r-=1
                else:
                    break
            else:
                break
                
        return score