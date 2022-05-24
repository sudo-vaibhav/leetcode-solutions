class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x,y = points[0]
        ans = 0
        
        for u,v in points[1:]:
            while x!=u or y!=v:
                if x==u or v==y:
                    if x==u:
                        if y<v:
                            y+=1
                        else:
                            y-=1
                    else:
                        if x<u:
                            x+=1
                        else:
                            x-=1
                else:
                    if y<v:
                        y+=1
                    else:
                        y-=1
                    if x<u:
                        x+=1
                    else:
                        x-=1
                ans+=1
                
        return ans