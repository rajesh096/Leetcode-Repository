class Solution {
public:
    int maxdif(vector<int>& nums, int l,int r,int size){
        if(l==r) return nums[l];
        int sl=nums[l] - maxdif(nums,l+1,r,size);
        int sr=nums[r] - maxdif(nums,l,r-1,size);
        return max(sl,sr);
    }
    bool predictTheWinner(vector<int>& nums) {
        int n=nums.size();
        return maxdif(nums,0,n-1,n) >=0;
    }
};