class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1,c2 = map(Counter,[s1,""])
        
        
        for i in range(len(s2)):
            cur = s2[i]
            c2[cur]+=1
            if i>=len(s1):
                c2[s2[i-len(s1)]]-=1
                if c2[s2[i-len(s1)]]==0:
                    del c2[s2[i-len(s1)]]
            if c2==c1:
                return True
        return False
            