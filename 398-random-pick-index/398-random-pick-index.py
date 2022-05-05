class Solution:

    def __init__(self, nums: List[int]):
        self.pos = defaultdict(list)
        for idx, num in enumerate(nums):
            self.pos[num].append(idx)

    def pick(self, target: int) -> int:
        indices = self.pos[target]
        randIdx = randint(0,len(indices)-1)
        # print(indices,randIdx)
        return indices[randIdx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)