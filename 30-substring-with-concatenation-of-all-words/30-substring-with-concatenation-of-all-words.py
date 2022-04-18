# overall complexity O(n.a.b + (a.b)^2) where a is number of words and b is length of each word and n is length of string
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         n = len(s) # O(1)
#         wordLen = len(words[0])  #O(1)
#         totalSubLen = wordLen*len(words) #O(1)
#         ws = set(words) 
#         words = Counter(words)
        
#         def check(idx):
#             end = idx+totalSubLen
#             x = {}
#             if end>n:
#                 return False
#             else:
#                 for i in range(idx,end,wordLen):
#                     temp = s[i:i+wordLen] 
#                     if temp not in ws:
#                         return False
#                     else:
#                         x[temp] = 1 if temp not in x else x[temp]+1
#                 return x==words
            
#         ans = []
#         for i in range(n):
#             if check(i):    
#                 ans.append(i)
#         return ans

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s) # O(1)
        wordLen = len(words[0])  #O(1)
        wc = len(words)
        totalSubLen = wordLen*wc #O(1)
        ws = set(words) 
        words = Counter(words)
        ans = []
        
        def slidingWindow(beg):
            wordsUsed = 0
            end = n
            x = defaultdict(int)
            right = beg
            while right<end:
                if right+wordLen>n:
                    break
                temp = s[right:right+wordLen]
                if temp not in words:
                    x = defaultdict(int)
                    beg = right + wordLen
                    wordsUsed = 0
                else:
                    x[temp] += 1
                    # wordsUsed+=1
                    if x[temp] > words[temp]:
                        while x[temp] > words[temp]:
                            leftString = s[beg:beg+wordLen]
                            x[leftString]-=1
                            beg+=wordLen
                            if leftString!=temp:
                                wordsUsed -= 1
                    else:
                        wordsUsed += 1
                    
                    if wordsUsed == wc:
                        ans.append(beg)
                right += wordLen
                    
                
        
        for beg in range(wordLen):
            slidingWindow(beg)
        
        return ans
        
        