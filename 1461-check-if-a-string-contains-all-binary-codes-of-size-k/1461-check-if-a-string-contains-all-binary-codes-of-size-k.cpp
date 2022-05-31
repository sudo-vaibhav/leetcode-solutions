class TrieNode{
    public:
    vector<TrieNode*> children;
    bool hasNum;
    TrieNode(){
        this->children = {NULL,NULL};    
        this->hasNum = false;
    }
};

class Solution {
    TrieNode* root;
    int trieSize;
    bool searchTrie(string& num){
        auto temp = root;
        for(auto& cur:num){
            if(temp->children[cur-'0']==NULL){
                return false;
            }
            else{
                temp = temp->children[cur-'0'];
            }
        }
        return temp->hasNum;
    }
    
    void insertTrie(string& num){
        auto temp = root;
        for(auto& cur:num){
            if(temp->children[cur-'0']==NULL){
                temp->children[cur-'0'] = new TrieNode();
            }
            temp = temp->children[cur-'0'];
        }
        temp->hasNum = true;
        trieSize++;
    }
    
public:
    
    bool hasAllCodes(string s, int k) {
        root = new TrieNode();
        trieSize = 0;
        int n = s.size();
        string window = "";
        for (int i = 0; i < n; i++)
        {
            window += string(1, s[i]);
            if (window.size() == k)
            {
                if(!searchTrie(window)){
                    insertTrie(window);
                }
            }
            if (i >= k - 1)
            {
                window.erase(window.begin());
            }
        }

        return trieSize==pow(2,k);
    }
};