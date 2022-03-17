struct TrieNode{
    TrieNode* children[2];
    TrieNode(){
        this->children[0]=nullptr;
        this->children[1]=nullptr;
    }
    void insert(int val){
        bitset<32> bs(val);
        TrieNode* temp = this;
        for(auto i=31;i>=0;i--){
            auto cur_bit = bs[i];
            if(temp->children[cur_bit]){
                
            }
            else{
                temp->children[cur_bit] = new TrieNode();
            }
            temp = temp->children[cur_bit];
        }
    }
    
    int searchClosestToComplement(int val){
        bitset<32> bs(val);
        TrieNode *temp = this;
        int ans = 0;
        for(auto i=31;i>=0;i--){
            auto cur_bit = !bs[i];
            if(!temp){ return -1;}
            if(temp->children[cur_bit]){
                ans|=(1<<i);
                temp = temp->children[cur_bit];
            }
            else{
                temp = temp->children[!cur_bit];
            }
            
            // ans<<=1;
        }
        return ans;
    }
};

struct Query{
    int num,cap,idx;
    Query(int n,int c, int i){
        num=n;cap=c;idx=i;
    }
};

class Solution {
public:
    vector<int> maximizeXor(vector<int>& nums, vector<vector<int>>& queries) {
        vector<Query> qs;
        for(auto i=0;i<queries.size();i++){
            auto t = queries[i];
            qs.push_back(Query(t[0],t[1],i));
        }
        sort(qs.begin(),qs.end(),[](Query q1,Query q2){
            return q1.cap<q2.cap;
        });
        sort(nums.begin(),nums.end());
        vector<int> res = vector<int>(queries.size());
        auto trie = new TrieNode();
        int i = 0;
        for(auto q:qs){
            while(nums[i]<=q.cap&&i<nums.size()){
                trie->insert(nums[i++]);
            }
            res[q.idx] = trie->searchClosestToComplement(q.num);
        }
        return res;
    }
};