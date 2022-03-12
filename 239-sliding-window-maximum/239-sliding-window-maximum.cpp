// another naive approach would have been to check elem by elem for every possible window (Brute force)

// O(n) time and O(n) space soln using deque
class Solution {
public:
    vector<int> maxSlidingWindow(const vector<int>& nums, const int &k) {
        // pair -> index , val
        deque<pair<int,int>> q;
        int n = nums.size();
        vector<int> ans(n-k+1);
        for(int i=0;i<n;i++){
            const auto cur = nums[i];
            while(!q.empty() && q.front().first<i-k+1){
                q.pop_front();
            }
            
            while(!q.empty()&&q.back().second<=cur){
                q.pop_back();
            }
            
            q.push_back({i,cur});
            if(i>=k-1){
                ans[i-k+1]=(q.front().second);
            }
        }
        return ans;
    }
};