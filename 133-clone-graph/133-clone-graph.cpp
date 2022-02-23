/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if(!node) return node;
        map<int,Node*> nodeMap;
        queue<Node*> q;
        q.push(node);
        nodeMap[node->val] = new Node(node->val);
        
        while(!q.empty()){
            auto curr = q.front();
            q.pop();
            
            auto dupNode = nodeMap[curr->val];
            
            for(auto i:curr->neighbors){
                if(!nodeMap.count(i->val)){
                    nodeMap[i->val] = new Node(i->val);
                    q.push(i);
                }
                
                dupNode->neighbors.push_back(nodeMap[i->val]);
            }
            
        }
        
//         for(auto n : nodeMap){
//             auto ans = n.second;
//             cout<<"node val: "<<ans->val<<" neighbours:"<<endl;
//             for(auto i:ans->neighbors) cout<<i->val<<"\t";
//             cout<<endl;
//         }
     
        return nodeMap[node->val];
        
    }
};