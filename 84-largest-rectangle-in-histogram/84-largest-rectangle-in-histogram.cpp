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
            // ,nextSmaller(n);
        
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
        
        s = stack<pair<int,int>>();
        
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
            
            maxArea = max(maxArea,cur*(temp-prevSmaller[i]-1));
            s.push({cur,i});
        }
        
        return maxArea;
        
    }
};