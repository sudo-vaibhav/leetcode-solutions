class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        r = defaultdict(int)
        c = defaultdict(int)
        m,n = len(picture),len(picture[0])
        for i in range(m):
            for j in range(n):
                cur = picture[i][j]
                if cur=="B":
                    r[i]+=1;c[j]+=1;
        
        ans = 0
        for i in range(m):
            for j in range(n):
                cur = picture[i][j]
                if cur=="B" and r[i]==1 and c[j]==1:
                    ans+=1
        return ans
                