class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp,target = map(list,[stamp,target])
        maxTurns = len(target)*10
        MADE, TODO = range(2)
        stampLen,targetLen = map(len,[stamp,target])
        windowData = []
        done = [False]*targetLen
        ans = []
        q = deque()
        for i in range(targetLen-stampLen+1):
            made,todo = set(),set()
            for j in range(stampLen):
                if stamp[j]==target[i+j]:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            
            windowData.append([made,todo])
            
            if not todo:
                ans.append(i)
                for j in range(i,i+stampLen):
                    if not done[j]:
                        q.append(j)
                        done[j] = True
            
        while q:
            i = q.popleft()
            
            for j in range(max(0,i-stampLen+1),min(targetLen-stampLen,i)+1):
                if i in windowData[j][TODO]:
                    windowData[j][TODO].remove(i)
                    
                    if not windowData[j][TODO]:
                        ans.append(j)
                        for m in windowData[j][MADE]:
                            q.append(m)
                            done[m]=True
                
        return ans[::-1] if all(done) else []
                