class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length()!=t.length()) return false;
        unordered_map<char,int> dic;
        for(int i=0;i<s.size();i++){
            dic[s[i]]++;
            dic[t[i]]--;
        }
        for (auto cnt:dic){
            if (cnt.second){
                return false;
            }
        }
        return true;
    }
};