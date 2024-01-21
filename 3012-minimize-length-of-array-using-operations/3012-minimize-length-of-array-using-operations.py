class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        mini = list(sorted(nums))[0]
        c = Counter(nums)[mini]
#         5 5 5 5 5
#         0 5 5 5
# 0 0 5

        # 1 1 -> 1
        # 5 5 5->5 0
        for a in nums:
            if a%mini:return 1
        return ceil(c/2)
#     [5,2,2,2,9,10] 1 
# 1 2 2 9 10
# 1 2 9 10
# 1 9 10
# 1 10
# 1




# [5,5,5,10,5]
# 5 5 5 0        5 5 5 5
# 5 0 0          0 5 5
# 5 0 0          0 0