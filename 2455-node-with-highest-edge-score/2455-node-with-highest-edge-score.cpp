class Solution {
public:
    int edgeScore(vector<int>& edges) {
        vector<long long> val(edges.size());
        for(int i=0;i<edges.size();i++){
            val[edges[i]]+=i;
        }
        int res=0;
        long long maxi = 0;
        for (int i=0;i<edges.size();i++){
            if(maxi<val[i]){
                res=i;
                maxi=val[i];
            }
        }
        return res;
    }
};