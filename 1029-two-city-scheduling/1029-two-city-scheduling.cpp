class Solution {
public:
    map<vector<int>,int> dp;
    int solve(int t,int pl, int pr,vector<vector<int>>& costs){
        if(dp.count({t,pl,pr})) return dp[{t,pl,pr}];
        if(pl==0 && pr==0) return dp[{t,pl,pr}]= 0;
        int s=0;
        if(pl==0){
            for(int i=0;i<t;i++){
                s+=costs[i][1];
            }
            return dp[{t,pl,pr}]=s;
        }
        else if(pr==0){
            for(int i=0;i<t;i++){
                s+=costs[i][0];
            }
            return dp[{t,pl,pr}]=s;
        }
        return dp[{t,pl,pr}]=min(costs[t-1][0]+solve(t-1,pl-1,pr,costs),
            costs[t-1][1]+solve(t-1,pl,pr-1,costs)
           );
    }
    
    int twoCitySchedCost(vector<vector<int>>& costs) {
        int n = costs.size()/2;
        dp = map<vector<int>,int>();
        return solve(2*n,n,n,costs);
    }
};