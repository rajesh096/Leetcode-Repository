class Solution {
public:
    vector<int> par;
    int find(int i){
        if(par[i] == i){
            return i;
        }
        return par[i] = find(par[i]);
    }
    void merge(int u, int v){
        int pu = find(u);
        int pv = find(v);
        if(pu!=pv){
            par[pv] = pu;
        }
    }
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        int n = s.size();
        par.resize(n);
        for(int i=0;i<n;i++){
            par[i] = i;
        }
        for(auto it : pairs){
            merge(it[0], it[1]);
        }
        unordered_map<int, vector<int>> mp;
        for(int i=0;i<n;i++){
            mp[find(i)].push_back(i);
        }
        // vector<int> ar;
        for(auto v : mp){
            string st;
            // ar = v.second;
            for(auto ch : v.second){
                st+=s[ch];
            }
            sort(st.begin(), st.end());
            for(int i=0;i<v.second.size();i++){
                s[v.second[i]] = st[i];
            }
        }
        return s;
    }
};