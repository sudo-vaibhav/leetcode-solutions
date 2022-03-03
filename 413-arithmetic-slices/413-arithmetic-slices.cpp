class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        vector<int> diffs;
        
        for(auto i=1;i<nums.size();i++){
            diffs.push_back(nums[i]-nums[i-1]);
        }
        
        // int prev = INT_MAX;
        int simCount = 1;
        int ans = 0;
        for(auto i=1;i<diffs.size();i++){
            if(diffs[i]==diffs[i-1]){
                simCount++;
            }
            else{
                auto numOfElems = simCount+1;
                // 1 2 3 4
                //  1 1 1
                
                // 3 to numOfElems
                // 
                
                for(auto atATime = 3;atATime<=numOfElems;atATime++){
                    ans += (numOfElems-atATime+1);
                }
                
                simCount = 1;
            }
        }
        
        auto numOfElems = simCount+1;
                // 1 2 3 4 5 7
                //  1 1 1 1 2
                
                // 3 to numOfElems
                // 
                
        for(auto atATime = 3;atATime<=numOfElems;atATime++){
            ans += (numOfElems-atATime+1);
        }
        return ans;
    }
};