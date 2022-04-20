class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        windowSize = n+1
        ans = 0
        ct = Counter(tasks)
        maxHeap = [-ct[i] for i in ct]
        # print(maxHeap)
        while maxHeap:
#             get windowsize most frequent left task types
            taskAtHand = []
            popped = 0
            while maxHeap and popped<windowSize:
                taskAtHand.append(heappop(maxHeap))
                popped+=1
            # print("tah",taskAtHand)
            
            for task in taskAtHand:
                curCount = -task
                curCount -= 1
                if curCount>0:
                    heappush(maxHeap,-curCount)
                    
            if maxHeap:
                ans += windowSize
            else:
                ans += len(taskAtHand)
            
                
        return ans