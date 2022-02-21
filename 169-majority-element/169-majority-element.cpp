class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int,int> occurenceCount;
        int n = nums.size();
        for(auto num: nums){
            occurenceCount[num]++;
        }
        
        int maxNum,maxCount=0;
        
        for(auto i:occurenceCount){
            if(i.second>maxCount){
                maxCount = i.second;
                maxNum = i.first;
            }
        }
        
        return maxNum;
    }
};