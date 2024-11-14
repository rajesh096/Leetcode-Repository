class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        int arr[1005];
        memset(arr,0,sizeof(arr));
        for(auto i:trips){
            arr[i[1]+1]+=i[0];
            arr[i[2]+1]-=i[0];
        }
        for(int j=1;j<1005;j++){
            arr[j]+=arr[j-1];
            if(arr[j]>capacity){
                return false;
            }
        }
        return true;
    }
};