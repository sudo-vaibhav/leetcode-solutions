class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        i = 0
        for child in g:
            while i<len(s):
                if child>s[i]:
                    i+=1
                else:
                    ans+=1
                    i+=1
                    break
                
        
        return ans