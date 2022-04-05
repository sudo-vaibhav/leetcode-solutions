class Solution {
public:
    long long best[1001];
    vector<int> dp;
    long long s(int n,int& changeTime,long long& maxL){
        if (n==0) return -changeTime;
        if (dp[n]!=-1) return dp[n];
        long long ans = INT_MAX;
        for(int lc=1;lc<=min((long long)n,maxL);lc++){
            ans = min(ans,best[lc]+s(n-lc,changeTime,maxL)+changeTime);
        }
        return dp[n]=ans;
    }
    int minimumFinishTime(vector<vector<int>>& tires, int changeTime, int numLaps) {
        memset(best,INT_MAX,sizeof(best));
        dp = vector<int>(numLaps+1,-1);
        for(int i=0;i<=numLaps;i++)best[i]=INT_MAX;
        long long maxL = 0;
        for(auto tire:tires){
            long long time = tire[0];
            long long a = tire[0];
            long long r = tire[1];
            long long curTime = a;
            for(long long lc=1;lc<=numLaps && curTime<changeTime+a;lc++){
                // cout<<a*pow(r,lc)<<" "<<time<<"\n";
                
                if(time<best[lc]){
                    best[lc]=time;
                }
                curTime *= r;
                time+= curTime;
                maxL = max(maxL,lc);
            }
            // best[lc] = min(best[lc],time);
        }
        
//         for(int i=1;i<=maxL;i++){
//             cout<<best[i]<<" ";
//         }
        
        return s(numLaps,changeTime,maxL);
        
    }
};