class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        int n = deck.size();
        vector<int> sdeck = deck;
        sort(sdeck.begin(),sdeck.end());
        vector<int> ans = vector<int>(n);
        deque<int> indices;
        for(int i=0;i<n;i++){
            indices.push_back(i);   
        }   
        
        for(auto card: sdeck){
            ans[indices.front()]=card;
            indices.pop_front();
            if(indices.size()){
                indices.push_back(indices.front());
                indices.pop_front();
            }
        }
        
        return ans;
    }
};