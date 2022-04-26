class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans,n = None,len(letters)
        l,r = 0,n-1
        while l<=r:
            guess = l+(r-l)//2
            if letters[guess]>target:
                ans = letters[guess]
                r = guess-1
            else:
                l = guess+1
        
        if ans==None:
            return letters[0]
        else:
            return ans
        