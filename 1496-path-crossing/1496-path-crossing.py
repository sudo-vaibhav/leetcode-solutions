class Solution:
    def isPathCrossing(self, path: str) -> bool:
        loc = [0,0]
        vis = set()
        vis.add((0,0))
        for d in path:
            diff = [inf,inf]
            if d=="N":
                diff = [1,0]
            elif d=="S":
                diff = [-1,0]
            elif d=="W":
                diff = [0,-1]
            else:
                diff = [0,1]
            
            loc = [loc[0]+diff[0],loc[1]+diff[1]]
            if tuple(loc) in vis:
                return True
            else:
                vis.add(tuple(loc))
        return False
                
        
        