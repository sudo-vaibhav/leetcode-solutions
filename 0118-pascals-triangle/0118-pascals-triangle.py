class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows==1: return [[1]]
        ans = [[1],[1,1]]
        
        for i in range(3,numRows+1):
            temp = [1]
            for i in range(len(ans[-1])-1):
                temp.append(ans[-1][i]+ans[-1][i+1])
            temp.append(1)
            ans.append(temp)
        return ans
                