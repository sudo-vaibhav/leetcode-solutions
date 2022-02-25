class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> ans = {1};
        auto prev = ans;
        for(int i=0;i<rowIndex;i++){
            ans.push_back(1);
            for(int j=1;j<ans.size()-1;j++){
                ans[j] = prev[j-1]+prev[j];
            }
            prev = ans;
        }
        
        return ans;
    }
};