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
   int d;
    map<int, deque<int>> q;
    void vlr(TreeNode *root)
    {
        if (root == NULL) return;
        if (d % 2 == 0) q[d].push_back(root->val);
        else q[d].push_front(root->val);
        d++;
        vlr(root->left);
        vlr(root->right);
        d--;
    }
    vector<vector<int>> zigzagLevelOrder(TreeNode *root)
    {
        vector<vector<int>> ans;
        d = 0;
        vlr(root);
        for (auto it : q) ans.push_back(vector<int>(make_move_iterator(it.second.begin()), make_move_iterator(it.second.end())));
        return ans;
    }
};