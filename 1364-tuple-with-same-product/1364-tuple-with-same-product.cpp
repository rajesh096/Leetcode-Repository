class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        unordered_map<int, int> mp;
        int n = nums.size();
        // mp.reserve(n*(n-1)/2);
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                int val = nums[i]*nums[j];
                mp[val] += 1;
            }
        }
        int res = 0;
        for(auto& [k,v]: mp){
            if(v > 1) res+=(v*(v-1)*4);
        }
        return res;
    }
};