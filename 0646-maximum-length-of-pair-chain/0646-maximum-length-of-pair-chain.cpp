class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        sort(pairs.begin(),pairs.end(),[](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1]; 
    });
        int mini1=pairs[0][0];
        int mini2=pairs[0][1];
        int res=1;
        for(int i=1;i<pairs.size();i++){
            if(!(mini2>=pairs[i][0])){
                res++;
                mini1=pairs[i][0];
                mini2=pairs[i][1];
            }
        }
        return res;
    }
};