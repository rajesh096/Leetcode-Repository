class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        unordered_map<int, int> mp;
        for(int i=0;i<nums.size();i++){
            for(int j=i+1;j<nums.size();j++){
                int val = nums[i]*nums[j];
                if(mp.find(val) != mp.end()){
                    mp[val]+=1;
                }
                else{
                    mp[val] = 1;
                }
            }
        }
        int res = 0;
        unordered_map<int, int>:: iterator p;
        for(p=mp.begin();p!=mp.end();p++){
            int val = p->second;
            if(val > 1) res+=(val*(val-1)*4);
        }
        return res;
    }
};