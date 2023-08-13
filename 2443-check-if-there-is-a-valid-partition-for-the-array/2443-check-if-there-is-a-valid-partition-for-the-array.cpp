class Solution {
public:
    int dp[100000];
    bool helper(int ind,vector<int>& nums){
        if(ind==nums.size()){
            return true;
        }
        if (dp[ind]!=-1){
            return dp[ind];
        }
        bool tw=false;
        if(ind+1<nums.size() && nums[ind]==nums[ind+1]){
            tw=helper(ind+2,nums);
        }
        bool thr=false;
        if(ind+2<nums.size() && nums[ind]==nums[ind+1] && nums[ind+1]==nums[ind+2]){
            thr=helper(ind+3,nums);
        }
        else if(ind+2<nums.size() && nums[ind+2]==nums[ind+1]+1 && nums[ind+1]==nums[ind]+1){
            thr=helper(ind+3,nums);
        }
        return dp[ind]=tw || thr ;
    }
    bool validPartition(vector<int>& nums) {
        memset(dp,-1,sizeof(dp));
        return helper(0,nums);
    }
};