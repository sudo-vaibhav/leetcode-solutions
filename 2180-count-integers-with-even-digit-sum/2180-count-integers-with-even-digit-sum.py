class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for n in range(1,num+1):
            s = sum(map(int,list(str(n))))
            if s%2==0:
                c+=1
        return c