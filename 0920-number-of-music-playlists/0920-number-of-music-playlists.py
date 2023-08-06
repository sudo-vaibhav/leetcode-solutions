class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
#         crit = k-1 # make without one guy, which will be repeatable later
#         anything_goes = goal-k
        
#         return math.perm(n,crit)*(anything_goes)**n
        MOD = 10**9+7
        dp = [[0 for _ in range(n+1)] for _ in range(goal+1)]
    
        dp[0][0] = 1
        
        for song_count in range(1,goal+1):
            for distinct_songs in range(1,min(song_count,n)+1):
                dp[song_count][distinct_songs] = (
                    dp[song_count-1][distinct_songs-1]*(n-(distinct_songs-1))
                )%MOD
                if distinct_songs>k:
                    dp[song_count][distinct_songs] = (
                        dp[song_count][distinct_songs] +
                        dp[song_count-1][distinct_songs]*(distinct_songs-k)
                    )%MOD
        
        return dp[goal][n]
                    