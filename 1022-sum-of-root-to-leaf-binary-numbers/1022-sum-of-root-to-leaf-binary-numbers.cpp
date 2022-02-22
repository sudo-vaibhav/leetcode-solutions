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
    int ans;
    void vlr(TreeNode* root, int val){
        if(root){
            int prev = val<<1;
            if(!root->left&&!root->right){
                ans+= prev+root->val;
            }
            else{
                vlr(root->left,prev+root->val);
                vlr(root->right,prev+root->val);
            }
        }
    }
    int sumRootToLeaf(TreeNode* root) {
        ans = 0;
        vlr(root,0);
        
        return ans;
    }
};