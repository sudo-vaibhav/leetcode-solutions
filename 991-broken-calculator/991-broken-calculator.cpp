class Solution {
public:
    int brokenCalc(long long x, int t) {
        int steps = 0;
        while(t>x){
            steps++;
            if(t%2==1){
                t++;
            }
            else{
                t/=2;
            }
        }
        return steps+x-t;
    }
};