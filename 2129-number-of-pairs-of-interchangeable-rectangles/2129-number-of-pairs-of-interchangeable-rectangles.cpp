class Solution {
public:
    long long interchangeableRectangles(vector<vector<int>>& rectangles) {
        long long res=0;
        unordered_map<double,int> dic;
        for(vector<int> i:rectangles){
            double x = static_cast<double>(i[0]) / static_cast<double>(i[1]);
            dic[x]+=1;
        }
        for(auto i=dic.begin();i!=dic.end();i++){
            long long a=i->second;
            res+=(a*(a-1))/2;
        }
        return res;
    }
};