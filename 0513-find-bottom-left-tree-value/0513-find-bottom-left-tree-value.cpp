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
    int findBottomLeftValue(TreeNode* root) {
        if((root->left==NULL)&(root->right==NULL)) return root->val;;
        int res=0;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int level=q.size();
            for(int i=0;i<level;i++){
                TreeNode* curr=q.front();
                q.pop();
                if(i==0){
                    res=curr->val;
                }
                if(curr->left) q.push(curr->left);
                if(curr->right) q.push(curr->right);
            }
        }
        return res;
    }
};