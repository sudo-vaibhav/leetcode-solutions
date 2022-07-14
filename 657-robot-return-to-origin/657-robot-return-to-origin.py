class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0,0]
        for m in moves:
            
            if m=="U":
                pos[0]+=1
            elif m=="D":
                pos[0]-=1
            elif m=="R":
                pos[1]+=1
            else:
                pos[1]-=1
            
        return pos == [0,0]
                