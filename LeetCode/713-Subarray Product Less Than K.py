# Q) 713. Subarray Product Less Than K
# https://leetcode.com/problems/subarray-product-less-than-k/description/
#code
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        prod = 1
        left = ans = 0
        for right,val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left+=1
            #print(nums[left:right+1],prod)
            ans+= (right - left) + 1
            #print(ans)
        return ans
        
        '''
        : Attempt #1
        : Brute Force O(n^2)
        dp = [[None]*len(nums) for i in range(len(nums))]
        count = 0
        for i in range(len(nums)):
            dp[i][i] = nums[i]
            if dp[i][i] <k:
                count+=1
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i!=j:
                    dp[i][j] = dp[i][j-1] * nums[j]
                    if dp[i][j] <k:
                        count+=1
        return count
        '''