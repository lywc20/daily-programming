/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root == NULL) {
            return 0;
        }
        else{
            int left_depth = maxDepth(root->left);
            int right_depth = maxDepth(root->right);
            if(left_depth > right_depth){
                return left_depth + 1;
            }
            else{
                return right_depth + 1;
            }
        }
    }
};