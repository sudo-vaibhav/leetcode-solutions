class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ctr = {5:0,10:0,20:0}
        
        for bill in bills:
            if bill==5:
                pass
            elif bill==10:
                if ctr[5]>0:
                    ctr[5]-=1
                else:
                    return False
            else:
                if ctr[10]>0 and ctr[5]>0:
                    ctr[10]-=1
                    ctr[5]-=1
                elif ctr[5]>2:
                    ctr[5]-=3
                else:
                    return False
            ctr[bill]+=1
            
        return True