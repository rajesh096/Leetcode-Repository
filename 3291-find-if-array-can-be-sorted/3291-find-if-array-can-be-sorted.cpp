class Solution {
public:
    bool canSortArray(vector<int>& nums) {
        vector<int> res;
        unordered_map<int,vector<int>> mp;
        int c=1;
        int prev=__builtin_popcount(nums[0]);
        mp[c].push_back(nums[0]);
        for(int i=1;i<nums.size();i++){
            int x=__builtin_popcount(nums[i]);
            if(prev==x){
                mp[c].push_back(nums[i]);
            }
            else{
                mp[++c].push_back(nums[i]);
                prev=x;
            }
        }
        for(int i=1;i<=c;i++){
            sort(mp[i].begin(),mp[i].end());
            res.insert(res.end(),mp[i].begin(),mp[i].end());
        }
        sort(nums.begin(),nums.end());
        return res==nums;
    }
};