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
    int ans,depth,maxDepth;
    
    void lrv(TreeNode* root){
        if(root){
            depth++;
            lrv(root->left);
            lrv(root->right);
            depth--;
            if(depth>maxDepth){
                maxDepth = depth;
                ans = root->val;
            }
            else if(depth==maxDepth){
                ans+= root->val;
            }
        }
        
    }
    int deepestLeavesSum(TreeNode* root) {
        maxDepth = depth = 0;
        ans = 0;
        lrv(root);
        return ans;
    }
};