class Solution {
public:
    int mySqrt(int x) {
        int l = 1,r=x;
        while(l<=r){
            long long m = l + (r-l)/2;
            long long temp = m*m;
            if(temp==x){
                return m;
            }
            else if(temp<x){
                l = m+1;
            }
            else{
                r = m-1;
            }
        }
        
        return l-1;
    }
};