class Solution {
public:
    bool canConstruct(string s, int k) {
        if(s.size()<k) return false;
        int val[26] = {};
        for(char i : s)val[i-'a']++;
        int odd = 0;
        for(int pair :val){
            if(pair%2==1) odd++;
        }
        if(odd>k) return false;
        return true;
    }
};