class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        e = list(sorted(heights))
        return sum([int(heights[i]!=e[i]) for i in range(len(heights))])