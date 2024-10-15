class Solution {
public:
    string reorganizeString(string s) {
        vector<char> b(s.begin(),s.end());
        unordered_map<char,int> freq;
        for (int barcode : b) {
            freq[barcode]++;
        }

        priority_queue<pair<int, char>> maxHeap;
        for (auto& e : freq) {
            maxHeap.push({e.second, e.first}); 
        }

        vector<char> result;
        
        while (maxHeap.size() > 1) {
            auto first = maxHeap.top(); maxHeap.pop();
            auto second = maxHeap.top(); maxHeap.pop();
            
            result.push_back(first.second);
            result.push_back(second.second);
            
            if (--first.first > 0) {
                maxHeap.push(first);
            }
            if (--second.first > 0) {
                maxHeap.push(second);
            }
        }
        
        if (!maxHeap.empty()) {
            
            result.push_back(maxHeap.top().second);
        }
        if(s.size()!=result.size()) return "";
        string res(result.begin(),result.end());
        return res;
    }
};