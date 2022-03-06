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
    vector<TreeNode*> allPossibleFBT(int n) {
        if(n==1) return {new TreeNode()};
        n--;
        vector<TreeNode*> ans;
        for(auto onLeft = 1;onLeft<n;onLeft++){
            auto l = allPossibleFBT(onLeft);
            auto r = allPossibleFBT(n-onLeft);
            for(auto left:l){
                for(auto right:r){
                    auto root = new TreeNode();
                    root->left = left;
                    root->right = right;
                    ans.push_back(root);
                }
            }
        }
        return ans;
    }
};