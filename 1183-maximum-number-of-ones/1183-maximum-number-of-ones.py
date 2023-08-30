class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        candidates = []
        
        for i in range(sideLength):
            for j in range(sideLength):
                perRowOccs = (width//sideLength)+((width%sideLength)>j)
                colOccs = (height//sideLength)+((height%sideLength)>i)
                candidates.append(perRowOccs*colOccs)
        candidates.sort(reverse=True)
        
        return sum(candidates[:maxOnes])