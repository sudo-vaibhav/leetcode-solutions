double getDist(vector<int>&a){
        return pow(pow(a[0],2)+pow(a[1],2),0.5);
}
bool comp(vector<int>& a, vector<int>& b)
{
    auto A=getDist(a),B=getDist(b);
    return A<B;
}

class Solution {
public:
    
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        nth_element(points.begin(),points.begin()+k,points.end(),comp);
        vector<vector<int>> ans;
        for (int i=0;i<k;i++){
            ans.push_back(points[i]);
        }
        
        return ans;
    }
};