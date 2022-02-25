// Approach one using additional vector
// class Solution {
// public:
//     int populateNumVec(string version, vector<int>& num){
//         int temp = 0;
//         for(auto i:version){
//             if(isdigit(i)){
//                 temp=temp*10+(i-'0');
//             }
//             else{
//                 num.push_back(temp);
//                 temp = 0;
//             }
//         }
        
//         num.push_back(temp);
//         return num.size();
//     }
//     int compareVersion(string version1, string version2) {
//         vector<int> num1,num2;
//         int N = populateNumVec(version1,num1);
//         int M = populateNumVec(version2,num2);
        
//         int i = 0;
//         while(i<max(N,M)){
//             auto v1 = 0;
//             auto v2 = 0;
            
//             if(i<N){
//                 v1 = num1[i];
//             }
//             if(i<M){
//                 v2 = num2[i];
//             }
            
//             cout<<v1<<" "<<v2<<"\n";
//             if(v1>v2){
//                 return 1;
//             }
//             else if(v2>v1){
//                 return -1;
//             }
            
//             i++;
//         }
        
//         return 0;
//     }
// };


// generator pattern, O(1) space
class Solution {
public:
   
    
    int getNextBlock(string version, int& idx, int N){
        int num = 0;
        if(idx==N) return 0;
        for(;idx<N;idx++){
            if(version[idx]=='.'){
                idx++;
                return num;
            }
            else{
                num = num*10 + (version[idx]-'0');
            }
        }
        
        return num;
    }
    int compareVersion(string version1, string version2){
        int i=0,j=0,n=version1.size(),m = version2.size();
        while(i<n||j<m){
            auto num1 = getNextBlock(version1,i,n);
            auto num2 = getNextBlock(version2,j,m);
            cout<<num1<<" "<<num2<<endl;
            if(num1<num2) return -1;
            else if(num1>num2) return 1;
        }
       return 0;
    }
};