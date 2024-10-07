class Solution {
public:
    string removeDuplicateLetters(string s) {
        unordered_map<char,int> mp;
        set<char> v;
        stack<char> res;
        for (int i = 0; i < s.length(); ++i) {
            mp[s[i]] = i;
        }

        for (int i = 0; i < s.length(); ++i) {
            char ch = s[i];

            if (v.count(ch)) continue;

            
            while (!res.empty() && res.top() > ch && mp[res.top()] > i) {
                v.erase(res.top());
                res.pop();
            }

            
            res.push(ch);
            v.insert(ch);
        }

        string result;
        while (!res.empty()) {
            result = res.top() + result;
            res.pop();
        }

        return result;
        }
};