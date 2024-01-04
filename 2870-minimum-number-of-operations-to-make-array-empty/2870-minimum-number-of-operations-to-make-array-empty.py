class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        # possibleSolves
        
        
        c = Counter(nums)
        # print(c)
        # 2,3,4,5,6,7,8,9,10,11
        ans = 0
        for i in c:
            # temp = 100
            if c[i]==1:
                return -1
            # elif c[i]==2 or c[i]==3:
            #     temp=1
            # elif c[i]==4: 
            #     temp= 2
            # else:
            temp = inf
            c3 = 0
            while c3*3<=c[i]:
                if (c[i]-c3*3)%2==0:
                    temp = min(temp,c3+(c[i]-c3*3)//2)
                c3+=1
            # print(i,c[i],temp)
            ans += temp
        return ans