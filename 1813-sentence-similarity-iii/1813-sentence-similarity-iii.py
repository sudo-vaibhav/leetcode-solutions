class Solution:
    def areSentencesSimilar(self,s1: str, s2: str) -> bool:
        return self.check(s1,s2) if len(s1)>len(s2) else self.check(s2,s1)
        # if self.check(s1,s2) or self.check(s2,s1):
        #     return True
        # return False
    def check(self,s1,s2):
        
        
        w1, w2 = map(lambda x:x.split(),[s1,s2])
        m,n = len(w1),len(w2)
        if w1[:n]==w2 or w1[-n:]==w2:
            return True
        
        
        q1,q2 = map(deque,[w1,w2])
        # print(q1,q2)
        while q1 and q2:
            if q1[0]==q2[0]:
                q1.popleft()
                q2.popleft()
            elif q1[-1]==q2[-1]:
                q1.pop()
                q2.pop()
            else:
                break
            
        return len(q2)==0
#         @cache
#         def solve(i,j,mis):
#             if mis==2:
#                 return False
#             if j==n:
#                 return (i==m) or mis==0
#             if i==m:
#                 return False
#             # else:
#             ans = False
#             if mis==0:
#                 # if not missed yet, can always afford to miss now and start from scratch
#                 ans = solve(i+1,0,1)
#             # else:
#             if w1[i]==w2[j]:
#                 ans = solve(i+1,j+1,mis)
#             else:

#                 while i<len(w1) and w1[i]!=w2[j]:
#                     i+=1
#                 ans = solve(i,j,mis+1)
#             # if i
#             return ans
#         return solve(0,0,0) or any([solve(k,0,1) for k in range(1,m)])
#         assume that s1 is the bigger sentence with more words
#         
#         c2 = Counter(w2)
#         breaks = 0
#         i = 0
#         while i<len(w1):
            
#             if c2[w1[i]]>0:
#                 c2[w1[i]]-=1
#                 i+=1
#             else:
#                 while i<len(w1) and c2[w1[i]]==0:
#                     i+=1
#                 breaks+=1
#         if breaks>1:
#             return False
#         return True