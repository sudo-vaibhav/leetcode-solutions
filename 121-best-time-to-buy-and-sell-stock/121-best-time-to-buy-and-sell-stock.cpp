// O(n) space and O(n) time complexity
// class Solution {
// public:
//     int maxProfit(vector<int>& prices) {
//         long n= prices.size();
//         if(n==1) return 0;
//         vector<long> maxPrices(n,INT_MIN);
//         for(auto i=n-2;i>=0;--i){
//             maxPrices[i] = max((long)prices[i+1],maxPrices[i+1]);
//         }
        
//         long maxProfit = 0;
//         for(long i=0;i<n;i++){
//             maxProfit = max(maxProfit,maxPrices[i]-prices[i]);
//         }
        
//         return maxProfit;
//     }
// };

// O(1) space and O(1) time complexity

class Solution{
    public:
        int maxProfit(vector<int>& prices){
            int minPrice = INT_MAX;
            int maxProfit = 0;
            for(auto price:prices){
                minPrice = min(minPrice,price);
                maxProfit = max(maxProfit,price-minPrice);
            }
            return maxProfit;
        }
};