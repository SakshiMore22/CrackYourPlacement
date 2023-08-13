class Solution {
public:
    bool helper(int ind,vector<int>& nums,vector<int>& dp){
        if(ind==nums.size()){
            return true;
        }
        if (dp[ind]!=-1){
            return dp[ind];
        }
        bool ans=false;
        if(ind+1<nums.size() && nums[ind]==nums[ind+1]){
            ans|=helper(ind+2,nums,dp);
        }
        if(ind+2<nums.size() && nums[ind]==nums[ind+1] && nums[ind+1]==nums[ind+2]){
            ans|=helper(ind+3,nums,dp);
        }
        else if(ind+2<nums.size() && nums[ind+2]==nums[ind+1]+1 && nums[ind+1]==nums[ind]+1){
            ans|=helper(ind+3,nums,dp);
        }
        
        return dp[ind]=ans;
    }
    bool validPartition(vector<int>& nums) {
        vector<int> dp(nums.size(),-1);
        return helper(0,nums,dp);
    }
};