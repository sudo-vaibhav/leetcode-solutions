class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m,n = len(pizza),len(pizza[0])
        MOD = (10**9+7)
        agg = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                cur = 1 if pizza[i-1][j-1]=="A" else 0
                agg[i][j]=cur+agg[i][j-1]+agg[i-1][j]-agg[i-1][j-1]
        # print(*agg,sep="\n")
        @cache
        def applesIn (start,end):
#             (0,2) (1,3)
            w,x,y,z = *start,*end
            # print(start,end,)
            # print("pos",agg[y][z],agg[w][x],"neg",agg[w][z],agg[y][x])
            ans = agg[y][z]+agg[w][x]-agg[w][z]-agg[y][x]
            # print("apples count",start,end,ans)
            return ans
            
        @cache
        def solve(start,end,cuts):
            if cuts==0: return int(applesIn(start,end)>0)
            r,c,endR,endC = *start,*end
            ans = 0
            
            for cutAtR in range(r+1,endR):
                apples = applesIn((r,c),(cutAtR,endC))
                if apples>0:               
                    # print("valid rc",(r,c),(cutAtR,endC))
                    ans = (ans+solve((cutAtR,c),(endR,endC),cuts-1))%MOD
            
            for cutAtC in range(c+1,endC):
                apples = applesIn((r,c),(endR,cutAtC))
                if apples>0:
                    ans = (ans+solve((r,cutAtC),(endR,endC),cuts-1))%MOD
                    
            return ans
                
        
        return solve((0,0),(m,n),k-1)