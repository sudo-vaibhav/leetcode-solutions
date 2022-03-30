class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        top,bottom,left,right=0,m-1,0,n-1        
        while top<=bottom:
            mid = top+(bottom-top)//2
            if target>=matrix[mid][0] and target<=matrix[mid][-1]:
                break
            else:
                if target<matrix[mid][0]:
                    bottom=mid-1
                else:
                    top=mid+1
        row = mid
        while left<=right:
            mid = left+(right-left)//2
            if matrix[row][mid]==target:
                return True
            else:
                if matrix[row][mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            
        return False
    
    