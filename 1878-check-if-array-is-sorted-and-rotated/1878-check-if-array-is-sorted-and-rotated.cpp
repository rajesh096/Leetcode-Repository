class Solution {
public:
    bool check(vector<int>& nums) {
        int f = nums[0];
        int tm = 0;
        for(int i=1;i<nums.size();i++){
            if(nums[i-1] > nums[i]){
                if(tm==0) tm=1;
                else{
                    return false;
                }
            }
            else if(tm==1 && nums[i]>f){
                return false;
            }
        }
        if(tm==1 && nums[nums.size()-1]>f) return false;
        return true;
    }
};