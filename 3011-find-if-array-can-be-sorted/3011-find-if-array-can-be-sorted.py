class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def countSetBits(n): 

            # base case 
            if (n == 0): 
                return 0

            else: 

                # if last bit set add 1 else 
                # add 0 
                return (n & 1) + countSetBits(n >> 1) 
        
#         t = list(sorted(nums))
# #         75,34,30
# #         30,34,75
#         for i in range(len(nums)):
#             t1,t2 = countSetBits(nums[i]),countSetBits(t[i])
#             print(nums[i],t[i],t1,t2)
#             if t1!=t2:
#                 return False
#         return True
        prev = []
        r = inf
        tot = []
        for i in range(len(nums)):
            temp =countSetBits(nums[i]) 
            if temp==r:
                prev.append(nums[i])
            else:
                tot.append(list(prev))
                prev = [nums[i]]
                r = temp
        tot.append(prev)
        return sorted(nums)==[j for sub in tot for j in sorted(sub)]
        
        
                