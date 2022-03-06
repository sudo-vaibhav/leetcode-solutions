// Memoisation solution recursive
class Solution {
public:
    long MOD = 1000000007;
    long numberOfWays(int toBePicked,int toBeDelivered,map<pair<int,int>,long>& dp){
        if(toBePicked==0 && toBeDelivered==0) return 1;
        if(
            toBePicked<0 || 
            toBeDelivered<0 || 
            toBeDelivered<toBePicked
        ){
            return 0;
        }
        
        if(dp.count({toBePicked,toBeDelivered})) return dp[{toBePicked,toBeDelivered}];
        
        // now find number of ways       
        // you can either pick now
        long ans = toBePicked * numberOfWays(toBePicked-1,toBeDelivered,dp);
        ans%=MOD;
        // or deliver now (you can only deliver picked)
        ans += (toBeDelivered-toBePicked)*numberOfWays(toBePicked,toBeDelivered-1,dp);
        ans%=MOD;
        return dp[{toBePicked,toBeDelivered}]=ans;
    }    
    int countOrders(int n) {
        int toBePicked = n;
        int toBeDelivered = n;
        map<pair<int,int>, long> dp;
        return numberOfWays(toBePicked,toBeDelivered,dp);
    }
};

// class Solution {
// private:
//     int MOD = 1e9 + 7;
//     vector<vector<int>> memo;
    
//     long totalWays(int unpicked, int undelivered) {
//         if (unpicked == 0 && undelivered == 0) {
//             // We have completed all orders.
//             return 1;
//         }
        
//         if (unpicked < 0 || undelivered < 0 || undelivered < unpicked) {
//             // We can't pick or deliver more than N items
//             // Number of deliveries can't exceed number of pickups 
//             // as we can only deliver after a pickup.
//             return 0;
//         }
        
//         if (memo[unpicked][undelivered]) {
//             // Return cached value, if already present. 
//             return memo[unpicked][undelivered];
//         }
        
//         long ans = 0;
        
//         // Count all choices of picking up an order.
//         ans += unpicked * totalWays(unpicked - 1, undelivered);
//         // Handle integer overflow.
//         ans %= MOD;
        
//         // Count all choices of delivering a picked order.
//         ans += (undelivered - unpicked) * totalWays(unpicked, undelivered - 1);
//         // Handle integer overflow.
//         ans %= MOD;
        
//         return memo[unpicked][undelivered] = ans;
//     }
    
// public:
//     int countOrders(int n) {
//         memo = vector<vector<int>> (n + 1, vector<int>(n + 1, 0));
//         return totalWays(n, n);
//     }
// };

// class Solution {
// public:
//     int MOD = 1e9 + 7;
    
//     int countOrders(int n) {
//         vector<vector<long>> dp (n + 1, vector<long>(n + 1, 0));

//         for (int unpicked = 0; unpicked <= n; unpicked++) {
//             for (int undelivered = unpicked; undelivered <= n; undelivered++) {
//                 // If all orders are picked and delivered then,
//                 // for remaining '0' orders we have only one way.
//                 if (unpicked == 0 && undelivered == 0) {
//                     dp[unpicked][undelivered] = 1;
//                     continue;
//                 }
                
//                 // There are some unpicked elements left. 
//                 // We have choice to pick any one of those orders.
//                 if (unpicked > 0) {
//                     dp[unpicked][undelivered] += unpicked * dp[unpicked - 1][undelivered];
//                 }
//                 dp[unpicked][undelivered] %= MOD;
                
//                 // Number of deliveries done is less than picked orders.
//                 // We have choice to deliver any one of (undelivered - unpicked) orders. 
//                 if (undelivered > unpicked) {
//                     dp[unpicked][undelivered] += (undelivered - unpicked) * dp[unpicked][undelivered - 1];
//                 }
//                 dp[unpicked][undelivered] %= MOD;
//             }
//         }
        
//         return dp[n][n];
//     }
// };