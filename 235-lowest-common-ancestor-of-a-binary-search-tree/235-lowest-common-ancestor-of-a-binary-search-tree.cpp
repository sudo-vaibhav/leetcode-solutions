/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root || p->val==root->val||q->val==root->val) return root;
        int pv = p->val,qv=q->val,v=root->val;
        if(pv>v && qv>v){
            return lowestCommonAncestor(root->right, p,q);
        }
        else if(pv<v && qv<v){
            return lowestCommonAncestor(root->left, p,q);
        }
        else{
            return root;
        }
    }
};