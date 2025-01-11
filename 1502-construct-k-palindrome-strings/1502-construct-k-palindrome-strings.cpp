class Solution {
public:
    bool canConstruct(string s, int k) {
        if(s.size()<k) return false;
        map<char,int> mp;
        for(char i : s) mp[i]++;
        int odd = 0;
        for(const auto& pair : mp){
            if(pair.second%2==1) odd++;
        }
        if(odd>k) return false;
        return true;
    }
};