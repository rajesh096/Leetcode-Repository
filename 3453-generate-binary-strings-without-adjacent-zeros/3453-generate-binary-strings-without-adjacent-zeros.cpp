class Solution {
public:
    void rec(int n, string s,vector<string> &res){
        if(s.size()==n){
            res.push_back(s);
            return;
        }
        if(s.size()==0 || s.back()=='1'){
            s+='0';
            rec(n, s, res);
            s.pop_back();
        }
        s+='1';
        rec(n, s, res);
        s.pop_back();
    }


    vector<string> validStrings(int n) {
        vector<string> res;
        rec(n, "", res);
        return res;
    }
};