class Solution {
public:
    vector<string> res;
    void helper(int o ,int c ,string s,int n){
        if (o==n && c==n){
            res.push_back(s);
            return;
        }
        if (o<n){
        helper(o+1,c,s+'(',n);
        }
        if (c<o){
        helper(o,c+1,s+')',n);
        }
    }
    vector<string> generateParenthesis(int n) {
        helper(0,0,"",n);
        return res;
    }
};