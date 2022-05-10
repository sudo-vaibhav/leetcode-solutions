class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m,n = len(mat),len(mat[0])
        l = 0
        r = m-1
        row = None
        while l<=r:
            guess = l+(r-l)//2
            minVal,maxVal = mat[guess][0],mat[guess][-1]
            if minVal<=target<=maxVal:
                row = guess
                break
            else:
                if target>maxVal:
                    l = guess+1
                else:
                    r = guess-1
        if row==None:
            return False
        
        l = 0
        r = n-1
        while l<=r:
            guess = l+(r-l)//2
            if mat[row][guess]==target:
                return True
            elif mat[row][guess]<target:
                l = guess+1
            else:
                r = guess-1
        
        return False
        