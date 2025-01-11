class Solution {
public:
    bool canConstruct(string s, int k) {
        map<char,int> mp;
        if(s.size()<k) return false;
        for(char i : s) mp[i]++;
        int odd = 0;
        for(const auto& pair : mp){
            if(pair.second%2==1) odd++;
        }
        
        if(odd>k) return false;
        return true;
    }
};