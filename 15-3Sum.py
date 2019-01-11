# Q) 3Sum
#	 https://leetcode.com/problems/3sum/description/
#code
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        : Attempt #2 
        """
        l=[]
        for i in range(len(nums)-1):
            s = set()
            for j in range(i+1,len(nums)):
                x= -(nums[i]+nums[j])
                if x in s:
                    l.append([x,nums[i],nums[j]])
                else:
                    s.add(nums[j])
        y = set()
       
        for itm in l:
            
            if tuple(sorted(itm)) not in y:
                y.add(tuple(sorted(itm)))
          
        return list(y)
        
        
        
        
        """
        
        '''
        : Attempt #1, Time Limit Exceeded
        '''
        nums = sorted(nums)
        l = []
        a = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    tmp = -(nums[i] + nums[j])
                    if -(nums[i] + nums[j]) in nums:
                        val = nums.index(tmp)
                        if val!=i and val!=j:
                            if tuple(sorted([nums[i],nums[j],tmp])) not in a:
                                l.append(([nums[i],nums[j],tmp]))
                                a.add(tuple(sorted([nums[i],nums[j],tmp])))
        return sorted(l)
        
        """
			