class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        // pair -> height, idx
        vector<pair<int,int>> h(n);
        for(int i=0;i<n;i++){
            h.push_back({heights[i],i});
        }
        
        stack<pair<int,int>> s;
        
        vector<int> prevSmaller(n);
        
        for(int i=0;i<n;i++){
            auto cur = heights[i];
            while(!s.empty()&&s.top().first>=cur){
                s.pop();
            }
            if(!s.empty()){
                prevSmaller[i] = s.top().second;
            }
            else{
                prevSmaller[i] = -1;
            }
            s.push({cur,i});
        }
        
        while(!s.empty()){
            s.pop();
        }
        
        int maxArea = 0;
        for(int i=n-1;i>=0;i--){
            auto cur = heights[i];
            int temp;
            while(!s.empty()&&s.top().first>=cur){
                s.pop();
            }
            if(!s.empty()){
                temp = s.top().second;
            }
            else{
                temp = n;
            }
            
            auto tempans = cur*(temp-prevSmaller[i]-1);
            if(tempans>maxArea){
                maxArea = tempans;
            }
            s.push({cur,i});
        }
        
        return maxArea;
        
    }
};