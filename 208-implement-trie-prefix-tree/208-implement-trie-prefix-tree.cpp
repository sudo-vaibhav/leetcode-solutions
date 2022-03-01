class Trie {
public:
    Trie* children[26];
    bool isTerminal;
    Trie() {
        // children = {NULL};
        for(auto i=0;i<26;i++) children[i]=NULL;
        isTerminal = false;
    }
    
    void insert(string word) {
        auto cur = this;
        for(auto i:word){
            if(!cur->children[i-'a']){
                cur->children[i-'a'] = new Trie();
            }
            cur = cur->children[i-'a'];
        }
        
        cur->isTerminal = true;
    }
    
    bool search(string word) {
        auto cur = this;
        for(auto i:word){
            if(!cur->children[i-'a']){
                return false;
            }
            cur = cur->children[i-'a'];
        }
        
        return cur->isTerminal;
    }
    
    bool startsWith(string prefix) {
        auto cur = this;
        for(auto i:prefix){
            if(!cur->children[i-'a']){
                return false;
            }
            cur = cur->children[i-'a'];
        }
        
        bool childrenExist = false;
        for(auto i:cur->children){
            if(i) {
                childrenExist = true;
                break;
            }
        }
        
        return childrenExist||cur->isTerminal;
        
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */