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
    vector<int> lvr(TreeNode* root){
        if(!root){
            return {INT_MAX,INT_MIN,0,true};
        }
        auto l = lvr(root->left);
        auto r = lvr(root->right);
        
        // if current subtree a bst
        vector<int> temp =  {
            min(root->val,min(l[MIN],r[MIN])),
            max(root->val,max(l[MAX],r[MAX])),
            root->val+l[SUM]+r[SUM],
            0
        };
    
        if(
            root->val>l[MAX]&&
            root->val<r[MIN]&&
            l[IS_BST]&&r[IS_BST]
        ){
            temp[3] = 1;
        }
        if (temp[IS_BST] && temp[SUM]>ans){
            ans = temp[SUM];
        }
        return temp;
    }
    
    int maxSumBST(TreeNode* root) {
        ans = 0;
        lvr(root);
        return ans;
        
    }
};