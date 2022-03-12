// another naive approach would have been to check elem by elem for every possible window (Brute force)

// O(n) time and O(n) space soln using deque
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        // pair -> index , val
        deque<pair<int,int>> q;
        vector<int> ans;
        for(int i=0;i<nums.size();i++){
            auto cur = nums[i];
            while(!q.empty() && q.front().first<i-k+1){
                q.pop_front();
            }
            
            while(!q.empty()&&q.back().second<=cur){
                q.pop_back();
            }
            
            q.push_back({i,cur});
            if(i>=k-1){
                ans.push_back(q.front().second);
            }
        }
        return ans;
    }
};