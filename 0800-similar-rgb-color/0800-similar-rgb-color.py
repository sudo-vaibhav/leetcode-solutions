class Solution:
    def similarRGB(self, color: str) -> str:
        color = color[1:]
        sections = color[:2],color[2:4],color[4:]
        sections = list(map(lambda x:int(x,16),sections))
        
        pos = range(16)
        def getDiff(u,v,w,x,y,z):
            return -(u-x)**2 - (v-y)**2 -(w-z)**2
        
        prev = (0,0,0)
        for first in pos:
            for second in pos:
                for third in pos:
                    
                    newNum = list(map(lambda x : 16*x+x,[first,second,third]))
                    # print(newNum)
                    diff = getDiff(*sections,*newNum)
                    if getDiff(*sections,*prev)<diff:
                        prev = newNum
        # print(getDiff(*sections,*prev))
        return "#"+"".join(list(map(lambda x:str(x)[2:].zfill(2),map(hex,prev))))