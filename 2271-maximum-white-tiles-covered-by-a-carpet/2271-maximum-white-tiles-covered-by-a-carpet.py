class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = len(tiles)
        l,r=0,0
        ans = 0
        maxAns = 0
        
        while r<n and maxAns<carpetLen:
            if r==l or tiles[l][0]+carpetLen>tiles[r][1]:
#                 we can expand the fully covered bit
                ans+=min(carpetLen,tiles[r][1]-tiles[r][0]+1)
                maxAns = max(ans,maxAns)
                r+=1
            else:
                partial = max(0,tiles[l][0]+carpetLen-tiles[r][0])
                maxAns = max(maxAns,ans+partial)
                ans-=tiles[l][1]-tiles[l][0]+1                
                l+=1
                
        
        return maxAns
        
            
            
        