class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        # def getMap(num):
        #     return 
        # if : return "A"
        temp = []
        while columnNumber>0:
            q = columnNumber%26 # 701 -> 25
            # if q==0:
            #     ans = "Z"+ans
            # else:
            # ans = chr(ord("A")+q)+ans 
            temp.append(q)
            columnNumber = (columnNumber)//26 # 26
            # if q==0:
            # if columnNumber=1:
                # if ans[0]!="Z":
                #     break
                
            # ans += getMap(q)
            # columnNumber -= q*26
        # if columnNumber:
        #     ans += getMap(columnNumber)
        temp = temp[::-1]
        # print(temp)
        for i in range(len(temp)-1,0,-1):
            if temp[i]==0:
                temp[i]="Z"
                temp[i-1]-=1
            else:
                temp[i] = chr(ord("A")+temp[i]-1)
        if temp[0]==0:
            temp[0]=""
        else:
            temp[0]=chr(ord("A")+temp[0]-1)
        # print()
        return "".join(temp)
        
        """
        
        ZY -> 26*26+25
        AB -> 26*1+2
        """