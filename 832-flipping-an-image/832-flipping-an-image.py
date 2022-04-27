class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row[:] = row[::-1]
            row[:] = [(1^i) for i in row]
        return image