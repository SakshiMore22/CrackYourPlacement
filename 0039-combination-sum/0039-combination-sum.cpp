class Solution {
public:
    vector<vector<int>> ans;
    void helper(int ind, vector<int>& nums,vector<int> a,int targ){
        if (targ==0){
            ans.push_back(a);
            return;
        }
        if (targ<0){
            return;
        }
        if (ind==nums.size()){
            return;
        }

        helper(ind+1,nums,a,targ);
        a.push_back(nums[ind]);
        helper(ind,nums,a,targ-nums[ind]);
        a.pop_back();
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> a;
        helper(0,candidates,a,target);
        return ans;
    }
};