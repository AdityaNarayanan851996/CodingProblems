// 			Q) 53. Maximum Subarray
// 			https://leetcode.com/problems/maximum-subarray/description/
//code
class Solution {
    public int maxSubArray(int[] nums) {
        if(nums.length > 0){
            
            int max_so_far = nums[0];
            int max_inside = 0;
            for(int i=0;i<nums.length;i++){
                max_inside += nums[i];
                if(max_so_far < max_inside){
                    max_so_far = max_inside;
                }
                if(max_inside < 0 ){
                    max_inside = 0;
                }
            }
            return max_so_far;
            
        }else{
            return 0;
        }
    }
}