class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        i = {k:0 for k in range(n)}
        
        for u,v in edges:
            i[v]+=1
        # print(i)
        temp = list(map(lambda x:x[0],filter(lambda x:x[1]==0,i.items())))
        # print(temp)
        [winner,*rest] = temp
        if len(rest):
            return -1
        return winner