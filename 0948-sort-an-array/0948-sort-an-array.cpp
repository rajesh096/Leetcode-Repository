class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        priority_queue<int,vector<int>,greater<int>> min_heap;
        for(auto i:nums) min_heap.push(i);
        vector<int> res;
        while(!min_heap.empty()){
            res.push_back(min_heap.top());
            min_heap.pop();
        }
        return res;
    }
};