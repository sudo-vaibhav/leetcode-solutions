class Solution:
    def minHeightShelves(self, books: List[List[int]], sw: int) -> int:
        # books.sort(key=lambda x:-x[1])
        # print(books)
        # ans = 0
        # cur = 0
        # curMax = 0
        # i = 0
        # while i<len(books):
        #     t,h = books[i]
        #     if cur+t<=sw:
        #         cur+=t
        #         curMax = max(curMax,h)
        #         i+=1
        #     else:
        #         cur = 0
        #         ans += curMax
        #         curMax = 0
        # return ans+curMax
        @cache
        def solve(i):
            if i>=len(books):
                return 0
            
            curMax = 0
            used = 0
            ans = inf
            for endShelf in range(i,len(books)):
                t,h = books[endShelf]
                used += t
                if used>sw:
                    break
                curMax = max(curMax,h)
                ans = min(ans,curMax+solve(endShelf+1))
            return ans
        return solve(0)
                
            
                
            