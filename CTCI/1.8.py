# Q) Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
#	 Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, 
# 	 write code to check if s2 is a rotation of s1 using only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).
#code
class Solution(object):
    def isRotation(self, s1,s2):
        """
        :type s1,s2: String
        :rtype: bool
        """
        if len(s1) != len(s2) or len(s1) == 0 or len(s2) == 0:
			return False
		
		elif len(s1) == len(s2):
			s11 = s1 + s1
			return self.isSubString(s11,s2)
		
		return False
			