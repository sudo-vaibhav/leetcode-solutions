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
    TreeNode* solve(vector<int>&nums, int l, int r){
        if(l>r){
            return NULL;
        }
        else{
            int m = l + (r-l)/2;
            auto root = new TreeNode(nums[m]);
            root->left = solve(nums,l,m-1);
            root->right = solve(nums,m+1,r);
            return root;
        }
    }
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        int l = 0,r = nums.size()-1;
        return solve(nums,l,r);
    }
};