class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int c=0;
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i]<=nums[i+1]) continue;
            if(c!=0) return false;
            
            if(i==0 or nums[i+1]>=nums[i-1]){
                nums[i]=nums[i+1];
                c++;
            }
            else{
                nums[i+1]=nums[i];
                c++;
            }
        }
        
        return true;
    }
};