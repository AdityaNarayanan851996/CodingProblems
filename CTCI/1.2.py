# Q) Write code to reverse a C-Style String. (C-String means that “abcd” is represented as five characters, including the null character.)

#code
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = ''
        for i in range(len(s)-1,-1,-1):
            
            r+=s[i]
        
        return r
    