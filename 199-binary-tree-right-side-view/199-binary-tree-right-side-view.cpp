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
    vector<int> ans;
    int d;
    int max_d;
    void vrl(TreeNode* root){
        if(root==nullptr) return;
         
        if(max_d<d){
            ans.push_back(root->val);
            max_d = d;
        }
        d++;
        vrl(root->right);
        vrl(root->left);
        d--;
       
    }
    
    vector<int> rightSideView(TreeNode* root) {
        d = 0;
        max_d = INT_MIN;
        
        vrl(root);
        return ans;
    }
};