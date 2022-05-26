class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        cnt = 0
        for i in range(0,n,2):
            v1,v2 = row[i],row[i+1]
            # couple = True
            # if v1%2==v2%2: couple = False
            # else:
            #     oddIdx = i if v1%2==1 else i+1
            #     evenIdx = i if oddIdx!=i else i+1
            #     oddPair = row[oddIdx]-1
            #     if oddPair!=row[evenIdx]:
            #         couple=False
            # if couple:
            #     continue
            # else:
            if v1%2==1:partner=v1-1
            else:partner=v1+1
            if v2==partner:continue
            for j in range(i+2,n):
                if row[j]==partner:
                    row[i+1],row[j] = row[j],row[i+1]
                    break
            cnt+=1
                
                
                
        return cnt