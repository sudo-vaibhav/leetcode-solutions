class Solution:
    def largestInteger(self, num: int) -> int:
        num = str(num)
        v1,v2 = [],[]
        oi=[]
        ei=[]
        for i, n in enumerate(num):
            if int(n)%2==0:
                v1.append(n)
                ei.append(i)
            else:
                v2.append(n)
                oi.append(i)
                
        v1.sort(reverse=True)
        v2.sort(reverse=True)
        ans = [""]*len(num)
        p1,p2=0,0
        for i in range(len(num)):
            if i in oi:
                ans[i]=v2[p1]
                p1+=1
            else:
                ans[i]=v1[p2]
                p2+=1
            
        return int("".join(ans))
                