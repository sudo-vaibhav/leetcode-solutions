class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # ans = 
        for row in image:
            row[:] = row[::-1]
            row[:] = [(0 if row[i]==1 else 1) for i in range(len(row))]
        return image