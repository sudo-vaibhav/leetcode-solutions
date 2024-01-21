from sortedcontainers import SortedList
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        
        arr = SortedList([(nums[i],i) for i in range(1,dist+2)])
        mini = s = sum(map(lambda x:x[0],arr[:k-1]))
        for i in range(dist+2,n):
            rec = (nums[i],i)
            temp = arr.bisect_right(rec)
            if temp<k-1:
                s -= arr[k-2][0] # remove the largest element
                s += nums[i] # add this new element from running sum
            arr.add(rec) # either way add this record
            leftmost = i-dist-1
            if leftmost>0:
                leftval = nums[leftmost]
                temprec = (leftval,leftmost)
                idx = arr.bisect_left(temprec)
                if idx>=k-1:
#                     wasnt included in s anyway
                    pass
                else:
#                     was included in s
                    s-=leftval
                    s+=arr[k-1][0]
                arr.pop(idx)
            mini = min(mini,s)
        return nums[0]+mini
#                     now this element cant be there

                    
                
#         arr = SortedList([(v, i + 1) for i, v in enumerate(nums[1:dist + 2])])
#         s = mi = sum(x[0] for x in arr[:k - 1])
        
#         for i in range(dist + 2, n):
#             v = nums[i]
#             # add
#             x = arr.bisect_right((v, i))
#             if x < k - 1:
#                 s -= arr[k - 2][0]
#                 s += v
#             arr.add((v, i))
#             # remove
#             io = i - dist - 1
#             if io > 0:
#                 vo = nums[io]
#                 xo = arr.bisect_left((vo, io))
#                 if xo >= k - 1:
#                     arr.pop(xo)
#                 else:
#                     s -= vo
#                     s += arr[k - 1][0]
#                     arr.pop(xo)
#             #
#             mi = min(mi, s)
        
#         return nums[0] + mi
        