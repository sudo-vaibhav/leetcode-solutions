/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    pair<int,TreeNode*> getLevel(TreeNode* root,int target,TreeNode* parent){
        if(!root) return {SHRT_MAX,NULL};
        if (root->val == target)return {0,parent};
        auto l = getLevel(root->left,target,root);
        auto r = getLevel(root->right,target,root);
        
        if (l.first<r.first){
            return {1+l.first,l.second};

        }
        else{
            return {1+r.first,r.second};
        }
    }
    bool isCousins(TreeNode* root, int x, int y) {
        auto t1=getLevel(root,x,NULL),t2=getLevel(root,y,NULL);
        // cout<<t1<<" "<<t2;
        return t1.first==t2.first && t1.second!=t2.second;
    }
};