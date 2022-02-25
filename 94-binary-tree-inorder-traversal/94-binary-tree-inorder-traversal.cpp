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
// O(n) time complexity and O(1) space complexity
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans;
        auto cur = root;
        while(cur!=nullptr){
            if(cur->left==nullptr){
                ans.push_back(cur->val);
                cur = cur->right;
            }
            else{
                auto prev = cur->left;
                while(prev->right&&prev->right!=cur){
                    prev = prev->right;
                }
                if(prev->right==nullptr){
                    prev->right = cur;
                    cur = cur->left;
                }
                else{
                    ans.push_back(cur->val);
                    prev->right = nullptr;
                    cur = cur->right;
                }
            }
        }
        return ans;
    }
};