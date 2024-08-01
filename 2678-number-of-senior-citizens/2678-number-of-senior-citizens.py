class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for d1,d2,d3,d4,d5,d6,d7,d8,d9,d0,g,a1,a2,s1,s2 in details:
            if int(a1+a2)>60:
                c+=1
        return c