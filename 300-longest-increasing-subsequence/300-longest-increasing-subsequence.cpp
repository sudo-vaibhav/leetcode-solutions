// My slow and weird approach, TLEs
// class Solution {
// public:
    
// pair<int, int> solve(int i, int sortedI, vector<int> &nums, vector<int> &sortedNums, map<pair<int, int>, pair<int, int>> &dp)
// {
//     if ((i == 0) || sortedI == 0)
//         return {0, -100000};
//     pair<int, int> ansPair = {i, sortedI};
//     if (dp.count({i, sortedI}))
//         return dp[{i, sortedI}];
//     if (nums[i - 1] == sortedNums[sortedI - 1] && solve(i - 1, sortedI - 1, nums, sortedNums, dp).second != nums[i - 1])
//     {
//         return dp[ansPair] = {1 + solve(i - 1, sortedI - 1, nums, sortedNums, dp).first, nums[i - 1]};
//     }
//     else
//     {
//         auto l = solve(i - 1, sortedI, nums, sortedNums, dp);
//         auto r = solve(i, sortedI - 1, nums, sortedNums, dp);

//         if (l.first > r.first)
//             return dp[ansPair] = l;
//         else if (l.first < r.first)
//             return dp[ansPair] = r;
//         else
//             return dp[ansPair] = l.second < r.second ? l : r;
//     }
// }
//     int lengthOfLIS(vector<int>& nums) {
//         map<pair<int, int>, pair<int, int>> dp;
//         vector<int> uniqueNums, sorted;
//         // sys.setrecursionlimit(25000)
//         map<int, int> freq;
//         for (auto num : nums)
//         {
//             freq[num]++;
//             if (freq[num] < 2)
//             {
//                 uniqueNums.push_back(num);
//             }
//         }
//         sorted = uniqueNums;
//         sort(sorted.begin(), sorted.end());
//         auto n = sorted.size();
//         // for (auto i : sorted)
//         // {
//         //     cout << i << "\t";
//         // }
//         // cout << endl;
//         // cout << << endl;
//         return  (solve(nums.size(), sorted.size(), nums, sorted, dp)).first;
//     }
// };





class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        auto n = nums.size();
        vector<int> dp(n,1);
        for(auto i=1;i<n;i++){
            for(auto j=0;j<i;j++){
                if(nums[i]>nums[j]){
                    dp[i] = max(dp[i],1+dp[j]);
                }
            }
        }
        
        return *max_element(dp.begin(),dp.end());
    }
};














































