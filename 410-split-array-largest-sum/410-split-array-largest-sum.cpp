class Solution {
public:
    vector<int> ps;
    map<pair<int,int>,int> dp;
    int n;
    int solve(int idx, int m){
        if(dp.count({idx,m})) return dp[{idx,m}];
        if(m==1){
            return ps[n]-ps[idx];
        } 
        int tempans = ps[n];
        for(int endAt=idx;endAt< n-m+1;endAt++){
            auto temp = ps[endAt+1]-ps[idx];
            tempans = min(tempans,max(
                solve(endAt+1,m-1),
                temp
            ));
            if (temp>tempans){
                break;
            }
        }
        
        return dp[{idx,m}]=tempans;
    }
    
    int splitArray(vector<int>& nums, int m) {
        ps = {0};
        dp = map<pair<int,int>,int>();
        int s = 0;
        n = nums.size();
        for(int i:nums){
            s+=i;
            ps.push_back(s);
        }
        
        return solve(0,m);
    }
};