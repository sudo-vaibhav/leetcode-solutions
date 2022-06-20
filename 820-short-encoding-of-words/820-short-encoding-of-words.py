class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        TR = lambda : defaultdict(TR)
        LONGEST = False
        tr = TR()
        
        for i in range(len(words)):
            word = words[i][::-1]
            tmp = tr
            for c in word:
                tmp = tmp[c]
                if LONGEST in tmp:
                    if len(word)>tmp[LONGEST]:
                        tmp[LONGEST]=len(word)
                else:
                    tmp[LONGEST] = len(word)
        
        def getAns(root):
            if len(root.keys())==1:
                return (root[LONGEST],1)
            else:
                ans = [0,0]
                for key in root:
                    if key!=LONGEST:
                        temp = getAns(root[key])
                        ans[0],ans[1] = ans[0]+temp[0],ans[1]+temp[1]
                return ans
                
        ans = 0
        for key in tr:
            temp = getAns(tr[key])
            ans += temp[0]+temp[1]
        return ans
        