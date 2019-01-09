# Q) 287. Find the Duplicate Number.
# https://leetcode.com/problems/find-the-duplicate-number/description/

#code
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = set()
        for i in range(len(nums)):
            if nums[i] in l:
                return nums[i]
            else:
                l.add(nums[i])
        