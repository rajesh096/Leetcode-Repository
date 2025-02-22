class Solution {
public:
    vector<int> par, size;

    void dsu(int n){
        for(int i=0;i<=n;i++){
            par[i] = i;
            size[i] = 1;
        }
    }

    int find(int val){
        if(val == par[val]){
            return val;
        }
        return par[val] =find(par[val]);
    }

    void dss(int u, int v){
        int pu = find(u);
        int pv = find(v);
        if(pu == pv) return;
        if(size[pu] < size[pv]){
            par[pu] = pv;
            size[pv]+=size[pu];
        }
        else{
            par[pv] = pu;
            size[pu]+=size[pv];
        }
    }

    int removeStones(vector<vector<int>>& stones) {
        int mini = 0, maxi = 0;
        for(auto s : stones){
            mini =  max(mini, s[0]);
            maxi =  max(maxi, s[1]);
        }
        par.resize(mini+maxi+2);
        size.resize(mini+maxi+2);
        dsu(mini+maxi+1);
        vector<int> arr(mini+maxi+2, 0);
        for(auto sto : stones){
            int u = sto[0];
            int v = sto[1]+mini+1;
            dss(u, v);
            arr[u]=1;
            arr[v]=1;
        }
        int count = 0;
        for(int i =0 ;i<arr.size();i++){
            if(arr[i]!=0 && par[i]==i){
                count++;
            }
        }
        int n = stones.size();
        return n - count;
    }
};