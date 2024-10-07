class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        for(int i=0;i<flowerbed.size();i++){
            int l,r;
            if(i==0) l=0;
            else l=flowerbed[i-1];
            
            if(i==(flowerbed.size())-1) r=0;
            else r=flowerbed[i+1];
            if(flowerbed[i]==0 && l==0 && r==0 && n>0){
                flowerbed[i]=1;
                n--;
            }
        }
        if(n) return false;
        return true;
    }
};