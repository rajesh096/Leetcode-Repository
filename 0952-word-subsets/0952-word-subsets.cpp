class Solution {
public:
    vector<string> wordSubsets(vector<string>& words1, vector<string>& words2) {
        vector<int> freq(26, 0);
        vector<string> result;
        for(string word: words2){
            vector<int> temp(26,0);
            for(int i=0;i<word.size();i++){
                temp[word[i]-'a']++;
            }
            for (int i=0;i<26;i++){
                freq[i] = max(freq[i],temp[i]);
            } 
        }
        for (string word: words1){
            bool universal = true;
            vector<int> temp(26, 0);
            for(int i=0;i<word.size();i++){
                temp[word[i]-'a']++;
            }
            for(int i=0;i<26;i++){
                if(freq[i]>temp[i]){
                    universal = false;
                    break;
                }
            }
            if(universal) result.push_back(word);
        }
        return result;
    }
};