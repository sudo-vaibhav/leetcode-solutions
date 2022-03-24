class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(),people.end());
        int i=0,j=people.size()-1,c=0;
        while(i<=j){
            if(i==j){
                c++;break;
            }
            if(people[j]+people[i]> limit){
                j--;
                c++;
            }else{
                i++;
                j--;
                c++;
            }
        }
        return c;
    }
};