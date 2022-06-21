# class Solution:
#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#         N = len(heights)
#         @cache
#         def furthest(idx,bricksLeft,laddersLeft):
#             if idx==N-1:
#                 return N-1
#             else:
#                 if heights[idx]>=heights[idx+1]:
#                     return furthest(idx+1,bricksLeft,laddersLeft)
#                 else:
#                     ans = idx
#                     bricksNeeded = heights[idx+1]-heights[idx]
#                     if bricksLeft>=bricksNeeded:
#                         ans = max(ans,furthest(idx+1,bricksLeft-bricksNeeded,laddersLeft))
#                     if laddersLeft>0:
#                         ans = max(ans,furthest(idx+1,bricksLeft,laddersLeft-1))
#                     return ans
#         return furthest(0,bricks,ladders)

# class Solution:
#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#         N = len(heights)
#         def KthLargestDiff(finalIdx,k):
#             heap = []
#             i=0
#             while i!=finalIdx:
#                 diff = heights[i+1]-heights[i]
#                 if diff>0:
#                     heappush(heap,diff)
#                 if len(heap)>k:
#                     heappop(heap)
#                 i+=1
#             print(heap,k)
#             return heap[0] if heap else inf
#         def isPos(finalIdx,ladderCutoff):
#             i = 0
#             laddersLeft,bricksLeft = ladders,bricks
#             while i!=finalIdx:
#                 cur,nex = heights[i],heights[i+1]
#                 diff = nex-cur
#                 if cur>=nex:
#                     pass
#                 else:
#                     if diff>=ladderCutoff and laddersLeft>0:
#                         laddersLeft-=1
#                     elif diff<=bricksLeft:
#                         bricksLeft-=diff
#                     # elif laddersLeft>0:
#                     #     laddersLeft-=1
#                     else:
#                         break
#                 i+=1
#             return i==finalIdx
#         l,r = 0,N-1
#         ans = 0
#         while l<=r:
#             guessIdx = (l+r)//2
#             diff = KthLargestDiff(guessIdx,ladders)
#             if isPos(guessIdx,ladderCutoff = diff):
#                 ans = max(ans,guessIdx)
#                 l = guessIdx+1
#             else:
#                 r = guessIdx-1
#         return ans

# from sortedcontainers import SortedList
# class Solution:
#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#         N = len(heights)
#         heap = []
#         i= 0
#         tot = 0
#         diffList = SortedList()
#         while i!=N-1:
#             cur,nex = heights[i],heights[i+1]
#             diff = nex-cur
#             if diff<=0:
#                 pass
#             else:
#                 tot+=diff
#                 diffList.add(diff)
#                 if ladders>0:
#                     end = sum(diffList[-ladders:])
#                 else:
#                     end = 0
#                 left = tot-end
#                 if left>bricks:
#                     break
#             i+=1
#         return i
        
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        laddersUsed = []
        i = 0
        while i<N-1:
            cur,nex = heights[i],heights[i+1]
            diff = nex-cur
            if diff>0:
#                 if ladder is left, always use ladder
                if ladders>0:
                    heappush(laddersUsed,diff)
                    ladders-=1
                else:
#                   now try to avoid using bricks (if a ladder was used previously for 
#                   a more trivial climb, swap uses instead)
                    if laddersUsed:
                        if laddersUsed[0]<diff and laddersUsed[0]<=bricks:
                            oldDiff = heappop(laddersUsed)
                            heappush(laddersUsed,diff)
                            bricks-=oldDiff
                        else:
                            if bricks>=diff:
                                bricks-=diff
                            else:
                                break
                    else:
                        if bricks>=diff:
                            bricks -= diff
                        else:
                            break
                        
            i+=1
        
        
        return i
        
        
        
        
        
        
        
        
        
        
        