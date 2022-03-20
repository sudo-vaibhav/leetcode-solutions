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

enum gh{
    MIN,MAX,SUM,IS_BST
};
class Solution {
public:
    int ans;
    // vector order -> min , max , sum, isBst
    void lvr(TreeNode* root, map<TreeNode*,vector<int>> &m){
        if(!root){
            m[root] = {INT_MAX,INT_MIN,0,true};
            return;
        }
        lvr(root->left,m);
        lvr(root->right,m);
        
        // if current subtree a bst
        auto l = root->left;
        auto r = root->right;
        vector<int> temp = {
            min(root->val,min(m[l][MIN],m[r][MIN])),
            max(root->val,max(m[l][MAX],m[r][MAX])),
            root->val+m[l][SUM]+m[r][SUM]
        };
    
        if(
            root->val>m[l][MAX]&&
            root->val<m[r][MIN]&&
            m[l][IS_BST]&&m[r][IS_BST]
        ){
            temp.push_back(true);
        }
        else{
            temp.push_back(false);
        }
        m[root] = temp;
        if (temp[IS_BST]){
            ans = max(ans,temp[SUM]);
        }
    }
    
    int maxSumBST(TreeNode* root) {
        ans = 0;
        map<TreeNode*,vector<int>> m;
        lvr(root,m);
        return ans;
        
    }
};