class Solution {
public:
    int countPrimes(int n) {
        if(n<=2){
            return 0;
        }
        vector<bool> cache(n,1);
        cache[0]=0;
        cache[1]=0;
        int c = n-2;
        
        for(int i=2;i<sqrt(n)+1;i++){
            if(cache[i]){
                for(int j=i*i;j<n;j+=i){
                    if(cache[j]){
                        cache[j] = 0; 
                        c--;
                    }
                }
           }
        }
        return c;
    }
};