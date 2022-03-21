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
    TreeNode* getOneBeforeRightMost(TreeNode* root){
        TreeNode *prev=NULL;
        while(root->right){
            prev = root;
            root = root->right;
        }
        return prev;
    }
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(root){
            if(root->val==key){
                if(!root->right) root = root->left;
                else if(!root->left) root = root->right;
                else{
                    auto temp = getOneBeforeRightMost(root->left);
                    if(!temp){
                        root->left->right = root->right;
                        root = root->left;
                    }
                    else{
                        auto newRoot = temp->right;
                        temp->right = temp->right->left;
                        newRoot->right = root->right;
                        newRoot->left = root->left;
                        
                        root = newRoot;
                    }
                }
            }
            else{
                if(root->val>key){
                    root->left = deleteNode(root->left,key);
                }
                else{
                    root->right = deleteNode(root->right,key);
                }
            }
        }
        
        return root;
    }
};