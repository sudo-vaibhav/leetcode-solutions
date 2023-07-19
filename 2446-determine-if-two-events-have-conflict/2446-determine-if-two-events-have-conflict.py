class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def d(v):
            return int("".join(v.split(":")))
        
        b1,e1,b2,e2 = map(d,[*event1,*event2])
        # print(b1,e1,b2,e2)
        if b1==b2 or e1==e2 or b1==e2 or b2==e1:
            return True
        if b1<b2:
            return e1>b2
        else:
            return e2>b1