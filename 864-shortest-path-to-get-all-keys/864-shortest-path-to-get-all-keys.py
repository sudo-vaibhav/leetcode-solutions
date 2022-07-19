class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m,n = len(grid),len(grid[0])
        row,col = None,None
        keyCount = 0
        for i in range(m):
            grid[i] = list(grid[i])
            for j in range(n):
                if grid[i][j] == "@":
                    row,col = i,j
                    grid[i][j] = "."
                elif grid[i][j].isalpha() and grid[i][j].islower():
                    keyCount+=1
        A = ord("A")
        a = ord("a")
        seen =  set()
        q = deque()
        init = (row,col,0,0)
        q.append(init)
        seen.add(init)
        steps = 0
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        allFound = (1<<keyCount)-1
        
        # print("kc",keyCount)
        while q:
            lenQ = len(q)
            # print(q)
            for _ in range(lenQ):
                
                cur = q.popleft()
                
                i,j,keyStatus,lockStatus = cur
                if keyStatus == allFound:
                    return steps
                for di,dj in moves:
                    I,J = i+di,j+dj
                    
                    if 0<=I<m and 0<=J<n and grid[I][J]!="#":
                        nex = grid[I][J]
                        newKeyStatus = keyStatus
                        newLockStatus = lockStatus
                        # if I==1 and J==0:
                            # print("status print",keyStatus,lockStatus)
                        allow = False
                        if nex==".":
                            # print("nex plain check",cur)
                            # if cur in seen:
                            #     print("already seen",cur)
                            allow = True
                        elif nex.isalpha() and nex.isupper(): # is lock
                            lockNo = ord(nex)-A
                            if (1<<lockNo)&keyStatus:
                                newLockStatus |= 1<<lockNo
                                allow = True
                        elif nex.isalpha() and nex.islower():
                            # print("keyfound",I,J,nex)
                            keyNo = ord(nex)-a
                            newKeyStatus |= 1<<keyNo
                            allow = True
                        
                        newTup = (I,J,newKeyStatus,newLockStatus) 
                        if allow and newTup not in seen:
                            # if newTup == :
                            #     print("getting inserted",I,J,steps)
                            seen.add(newTup)
                            q.append(newTup)
            steps+=1
        # print("final check",(1, 0, 5, 5) in seen)
        return -1
                            
                            
                        