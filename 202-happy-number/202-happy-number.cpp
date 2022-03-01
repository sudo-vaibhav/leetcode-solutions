class Solution {
public:
    bool isHappy(int n) {
        auto prev = INT_MAX;
        set<int> seen;
        while(!seen.count(n)){
            seen.insert(n);
            auto temp = n;
            auto ans = 0;
            while(temp>0){
                ans += pow(temp%10,2);
                temp/=10;
            }
            // prev = n;
            n = ans;
        }
        
        return n==1;
    }
};