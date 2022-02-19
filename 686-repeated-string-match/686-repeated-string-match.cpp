class Solution {
public:
    int repeatedStringMatch(string a, string b) {
        string expandedA=a;
        while(expandedA.size()<=pow(10,4)){
            expandedA+=a;
        }
        auto foundAt = expandedA.find(b); 
        if(foundAt==string::npos){
            return -1;
        }
        else{
            auto endAt = foundAt + b.size()-1;
            
            int startA = ceil(foundAt/a.size());
            int endA = ceil(endAt/a.size());
            
            return endA-startA+1;
        }
    }
};