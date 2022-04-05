class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int l =0;
        int r = n-1;
        int ma = 0;
        while(l<=r){
            int t = (r-l)*min(height[l],height[r]);
            ma = max(t,ma);
            if(height[l]>=height[r]){
                r--;
            }
            else
            {
                l++;
            }
        }
        return ma;
    }
};