class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s)+1
        ans = [i for i in range(1,n+1)]
        
        i = 0
        while i<len(s):

            if s[i]=="I":
                i+=1
            else:
                j = i
                while j<len(s) and s[j]=="D":
                    j+=1
                ans[i:j+1]=ans[i:j+1][::-1]
#               [1,2,3,4,5]
                i=j
            
        return ans
#         If i encounter,
#         if d encounter, lexicographically smallest ke liye pick smallest poss