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
    
    int widthOfBinaryTree(TreeNode* root) {
         queue<pair<TreeNode *, long long>> q;
        if (root == NULL)
            return 0;
        q.push({root, 0});
        int ans = 0;
        while (!q.empty())
        {
            auto f = q.front();
            int mmin = f.second;
            auto n = q.size();
            int last, first;
            for (int i = 0; i < n; i++)
            {
                auto cur = q.front();
                q.pop();
                auto adj = cur.second - mmin;
                auto node = cur.first;
                if (i == 0)
                {
                    first = adj;
                }
                last =adj;
                if (node->left)
                {
                    q.push({node->left, 2 * adj + 1});
                }
                if (node->right)
                {
                    q.push({node->right, 2 * adj + 2});
                }
            }
            ans = max(last - first + 1, ans);
        }
        return ans;
    }
};