class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        d = defaultdict(lambda : [0,0])
        
        for word in words:
            sortedWord = tuple(sorted(word))
            word = tuple(word)
            if word==word[::-1]:
                minVal = min(d[sortedWord])
                place = d[sortedWord].index(minVal)
                d[sortedWord][place]+=1
            elif word==sortedWord:
                d[sortedWord][0]+=1
            else:
                d[sortedWord][1]+=1
        # print(d)
        ans = 0
        for key in d:
            pairs = min(d[key])
            ans += 4*pairs
            for i in range(2):
                d[key][i]-=pairs
        
#         check for any free middle element
        for key in d:
            if key==key[::-1] and d[key][0]>0:
                ans+=2
                break
        
        return ans
            