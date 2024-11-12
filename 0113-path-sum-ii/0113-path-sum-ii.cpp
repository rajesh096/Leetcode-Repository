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
    void func(TreeNode* root, int ts, int s, vector<int> &arr, vector<vector<int>> &res){
        if(!root) return;
        s+=root->val;
        arr.push_back(root->val);
        if(!root->left and !root->right){
            if(s==ts){
                res.push_back(arr);
            }
        }
        else
            if(root->left) func(root->left,ts,s,arr,res);
            if(root->right) func(root->right,ts,s,arr,res);
        arr.pop_back();
    }

    vector<vector<int>> pathSum(TreeNode* root, int ts) {
        vector<vector<int>> res;
        vector<int> arr;
        int s=0;
        func(root,ts,s,arr,res);
        return res;
    }
};