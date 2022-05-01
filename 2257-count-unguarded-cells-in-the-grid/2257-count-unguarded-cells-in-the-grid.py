class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        guards = set(map(tuple,guards))
        walls = set(map(tuple,walls))
        guarded = set()
        intents = set()
        
        def allowed(i,j,intent):
            cell = (i,j)
            return 0<=i<m and 0<=j<n and (not ((cell in guards) or (cell in walls) or ((i,j,*intent) in intents)))
        def apply(baseCell,diff):
            i,j = baseCell
            di,dj = diff
            while allowed(i+di,j+dj,diff):
                # print(i+di,j+dj)
                i+=di
                j+=dj
                intents.add((i,j,*diff))
                guarded.add((i,j))
        
        diffs = [(-1,0),(1,0),(0,1),(0,-1)]
        for gc in guards:
            for diff in diffs:
                
                apply(gc,diff)
        # print(guarded)
        # print("\n")
        return m*n-len(guarded)-len(walls)-len(guards)
                
                