// Recursive 3D DP solution
// class Solution {
// public:
//     map<vector<int>,int> dp;
//     int solve(int t,int pl, int pr,vector<vector<int>>& costs){
//         if(dp.count({t,pl,pr})) return dp[{t,pl,pr}];
//         if(pl==0 && pr==0) return dp[{t,pl,pr}]= 0;
//         int s=0;
//         if(pl==0){
//             for(int i=0;i<t;i++){
//                 s+=costs[i][1];
//             }
//             return dp[{t,pl,pr}]=s;
//         }
//         else if(pr==0){
//             for(int i=0;i<t;i++){
//                 s+=costs[i][0];
//             }
//             return dp[{t,pl,pr}]=s;
//         }
//         return dp[{t,pl,pr}]=min(costs[t-1][0]+solve(t-1,pl-1,pr,costs),
//             costs[t-1][1]+solve(t-1,pl,pr-1,costs)
//            );
//     }
    
//     int twoCitySchedCost(vector<vector<int>>& costs) {
//         int n = costs.size()/2;
//         dp = map<vector<int>,int>();
//         return solve(2*n,n,n,costs);
//     }
// };


// refund concept
// class Solution{
//   public:
//   int twoCitySchedCost(vector<vector<int>>& costs) {
//         int n = costs.size();
//         vector<int> init = {0, 0};
//         auto cumulationRes = accumulate(
//             costs.begin(), costs.end(), init, 
//             [](vector<int> X, vector<int> Y){
//                 vector<int> res= {X[0] + Y[0], 0};
//                 return res; 
//             }
//         );
//         int cost = cumulationRes[0];
//         vector<int> benefitsOfTransfering(n);
//         for (int i = 0; i < n; i++)
//         {
//             benefitsOfTransfering[i] = costs[i][0] - costs[i][1];
//         }

//         sort(benefitsOfTransfering.begin(), benefitsOfTransfering.end());
//         for (int i = n / 2; i < n; i++)
//         {
//             cost -= benefitsOfTransfering[i];
//         }
//         return cost;
//     }
// };


// refund concept quick select approach
class Solution{
  public:
  int twoCitySchedCost(vector<vector<int>>& costs) {
      const int n = costs.size();  
      nth_element(costs.begin(),costs.begin()+n/2,costs.end(),
                  [](const vector<int>&a,const vector<int>&b){
                        return a[0]-a[1]<b[0]-b[1];
      });
      
      int s = 0;
      for (int i=0;i<n/2;i++){
        s+=costs[i][0]+costs[i+n/2][1];
      }
      return s;
    }
};