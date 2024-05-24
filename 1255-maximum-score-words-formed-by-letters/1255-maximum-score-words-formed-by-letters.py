class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        def solve(i,c):
            if i==len(words):
                return 0
            cur = words[i]
            t = Counter(cur)
            pos = True
            ans = solve(i+1,c)
            for k in t:
                if k in c and c[k]>=t[k]:
                    pass
                else:
                    pos = False
                    break
            if pos:
                for k in t:
                    c[k]-=t[k]
                
                ans = max(ans,sum(map(lambda x:score[x],map(lambda x:ord(x)-ord("a"),cur)))+ solve(i+1,c))
                for k in t:
                    c[k]+=t[k]
                
            return ans
                
        return solve(0,Counter(letters))