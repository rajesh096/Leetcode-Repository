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
    vector<int> largestValues(TreeNode* root) {
        vector<int> ar;
        if(root==NULL) return ar;
        
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            int max=INT_MIN;
            int level=q.size();
            for(int i=0;i<level;i++){
                TreeNode* cur=q.front();
                if(max<=cur->val){
                    max=cur->val;
                }
                q.pop();
                if(cur->left) q.push(cur->left);
                if(cur->right) q.push(cur->right);
            }
            ar.push_back(max);
        }
        return ar;
    }
};