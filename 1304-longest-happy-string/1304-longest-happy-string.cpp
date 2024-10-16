class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        unordered_map<char,int> mp;
        mp['a']=a;
        mp['b']=b;
        mp['c']=c;
        priority_queue<pair<int,char>> mh;
        for(auto i:mp){
            if(i.second>0) mh.push({i.second, i.first});
        }
        string res;
        while(!mh.empty()){
            auto f=mh.top();mh.pop();
            // auto s=mh.top();mh.pop();
            // int x=2,y=2;
            // while(f.first!=0 and x>0){
            //     res+=f.second;
            //     f.first--;
            //     x--;
            // }
            // while(s.first!=0 and y>0){
            //     res+=s.second;
            //     s.first--;
            //     y--;
            // }
            // if(f.first>0) mh.push(f);
            // if(s.first>0) mh.push(s);
            if(res.size()>=2 && res[res.size()-1]==f.second && res[res.size()-2]==f.second){
                if(mh.empty()) break;

                auto s=mh.top(); mh.pop();
                res+=s.second;
                s.first--;
                if(s.first>0) mh.push(s);
                mh.push(f);
            }
            else{
                int times=min(2,f.first);
                res+=string(times,f.second);
                f.first-=times;
                if(f.first>0) mh.push(f);
            }
        }
        return res;
    }
};