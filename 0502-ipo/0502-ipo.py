class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        arr = []
        for i in range(len(profits)):
            arr.append((capital[i],-profits[i]))
        
        arr.sort()
        # print("bruh",arr)
        # ans = 0
        canDo = []
        i = 0
        while k:
            while i<len(profits) and arr[i][0]<=w:
                heappush(canDo,(arr[i][1],arr[i][0]))
                i+=1
            if len(canDo):
                gain,_ = heappop(canDo)
                gain*=-1
                if gain>0:
                    # w-=cost
                    w+=gain
                # print("new w",w)
            k-=1
            # print("new w",w)
        
        return w