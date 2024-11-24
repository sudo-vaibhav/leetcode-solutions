class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        fin = []
        for row in matrix:
            fin.extend(row)
        fin.sort()
        negC = list(filter(lambda x:x<0,fin))
        # print(negC)
        if len(negC)%2==0:
            return sum(map(abs,fin))
        else:
            absVals = list(map(abs,fin))
            absVals.sort()
            return -absVals[0]+sum(absVals[1:])
            l1 = list(map(abs,negC[:-1]))
            e1 = negC[-1] if 0 not in fin else -negC[-1]
            l2 = list(filter(lambda x:x>0,fin))
            # print(l1,e1,l2)
            return sum([*l1,e1,*l2])