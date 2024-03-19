class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        timer = 0
        
        avail = []
        banned = []
        c = Counter(tasks)
        
        for k in c:
            heappush(avail,(-c[k],k))
            
        while banned or avail:
            while banned and banned[0][0]<=timer:
                pastFreed = True
                _,negcou,char = heappop(banned)
                # print("popped",char,"from banned with",negcou)
                heappush(avail,(negcou,char))
            # print("timer:",timer)
            if avail:
                negcou, char = heappop(avail)
                # print("popped",char,"from avail with",negcou)
                if negcou!=-1:
                    heappush(banned,(timer+n+1,negcou+1,char))
                timer+=1
            else:
                # pastFreed = False
                
                # if pastFreed==False:
                t,negcou,char=heappop(banned)
                timer = max(t,timer)
                heappush(avail,(negcou,char))
                # print("popped",char,"from banned with",negcou,"without pastfreed")
        return timer