# Q) 324. Wiggle Sort II
#	 https://leetcode.com/problems/wiggle-sort-ii/description/
#code
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        s_nums = sorted(nums)
        if len(nums) % 2 == 0:
            mid = int(len(nums)/2)
        else:
            mid = int(len(nums)/2) + 1
        left = sorted(s_nums[0:mid],reverse=True)
        right = s_nums[mid:]
        j = 0
        k = len(right)
        for i in range(len(s_nums)):
            
            if i%2 == 0:
                nums[i] = left[j]
                j+=1
            else:
                nums[i] = right[k-1]
                k-=1		