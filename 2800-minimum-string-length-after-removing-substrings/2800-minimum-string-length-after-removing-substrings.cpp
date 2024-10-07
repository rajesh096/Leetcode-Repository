class Solution {
public:
    int minLength(string s) {
        while(true){
            bool f=true;
            auto po1=s.find("AB");
            auto po2=s.find("CD");
            if(po1!=string::npos){
                s.erase(po1,2);
                f=false;
            }
            else if(po2!=string::npos){
                s.erase(po2,2);
                f=false;
            }
            else 
                return s.size();
        }   
    }
};