class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        t = list(map(int,current.split(":")))
        a=t[0]*60+t[1]
        t2 = list(map(int,correct.split(":")))
        b = t2[0]*60+t2[1]
        
        def f(diff):
            if diff>=60:
                return 60
            elif diff>=15:
                return 15
            elif diff>=5:
                return 5
            else:
                return 1
        print(b,a)
        diff = b-a
        print(diff)
        steps=0
        while diff>0:
            d = f(diff)    
            diff-=d
            steps+=1
        return steps