class Solution {
public:
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        long long mas=mass;
        sort(asteroids.begin(),asteroids.end());
        if(mass<asteroids[0]) return false;
        mas+=asteroids[0];
        for(int i=1;i<asteroids.size();i++){
            if(mas<asteroids[i]) return false;
            mas+=asteroids[i];
        }
        return true;
    }
};