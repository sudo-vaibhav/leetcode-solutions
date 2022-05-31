class TrieNode{
    public:
    TrieNode* children[2];
    bool hasNum;
    TrieNode(){
        this->children[0]=NULL;
        this->children[1]=NULL;
        this->hasNum = false;
    }
};

class Solution {
    TrieNode* root;
    unsigned int trieSize;    
    void insertTrie(deque<char>& num){
        auto temp = root;
        for(auto& cur:num){
            if(temp->children[cur-'0']==NULL){
                temp->children[cur-'0'] = new TrieNode();
            }
            temp = temp->children[cur-'0'];
        }
        if(!temp->hasNum){        
            temp->hasNum = true;
            trieSize++;
        }
    }
    
public:
    
    bool hasAllCodes(string s, int k) {
        root = new TrieNode();
        trieSize = 0;
        auto n = s.size();
        deque<char> window;
        for (auto i = 0; i < n; i++)
        {
            window.push_back(s[i]);
            if (window.size() == k)
            {
                insertTrie(window);
            }
            if (i >= k - 1)
            {
                window.pop_front();
            }
        }

        return trieSize==1<<k;
    }
};