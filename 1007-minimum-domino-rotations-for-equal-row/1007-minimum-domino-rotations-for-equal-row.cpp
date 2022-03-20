class Solution {
public:
    int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
        int c[6] = {0,0,0,0,0,0};
        int tc[6] = {0,0,0,0,0,0};
        int bc[6] = {0,0,0,0,0,0};
        int n = bottoms.size();
        for (auto i=0;i<n;i++){
            if(tops[i]==bottoms[i]){
                c[tops[i]-1]++;
            }
            else{
                c[tops[i]-1]++;
                c[bottoms[i]-1]++;
            }
            tc[tops[i]-1]++;
            bc[bottoms[i]-1]++;
        }
        
        bool flag = false;
        for(auto i=0;i<6;i++){
            if(c[i]==n){
                flag = true;
                break;
            }
        }
        if(flag){
            for(auto i=0;i<6;i++){
                if(c[i]==n){
                    return min(n-tc[i],n-bc[i]);
                }
            }   
        }
        else{
            return -1;
        }
        
        return 0;
    }
};