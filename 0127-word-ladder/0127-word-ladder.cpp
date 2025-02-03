class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        queue<pair<string, int>> q;
        unordered_set<string> s(wordList.begin(), wordList.end());
        s.erase(beginWord);
        q.push({beginWord, 1});
        while(!q.empty()){
            string w = q.front().first;
            int step = q.front().second;
            q.pop();
            if(w==endWord) return step;
            for(int i=0;i<w.size();i++){
                char ch = w[i];
                for(char j='a';j<='z';j++){
                    w[i] = j;
                    if(s.find(w)!=s.end()){
                        s.erase(w);
                        q.push({w,step+1});
                    }
                }
                w[i] = ch;
            }
        }
        return 0;
    }
};