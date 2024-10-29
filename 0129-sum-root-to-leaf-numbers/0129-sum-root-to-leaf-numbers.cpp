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
    void func(TreeNode* curr,vector<int> &arr,int val){
        if(!curr){
            arr.push_back(val);
            return;
        }
        val=val*10 + curr->val;
        if(!curr->left && !curr->right){
            arr.push_back(val);
            return;
        }
        if(curr->left) func(curr->left,arr,val);
        if(curr->right) func(curr->right, arr, val);
    }
    int sumNumbers(TreeNode* root) {
        vector<int> arr;
        func(root,arr,0);
        int s=0;
        for(int i:arr){
            s+=i;
        }
        return s;
    }
};