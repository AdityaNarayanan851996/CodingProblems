# Q) Write a method to decide if two strings are anagrams or not.
#code
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """      
        '''
        Solution #1 (Faster)
        '''
        a = sorted(s)
        b = sorted(t)
        
        if a == b:
            return True
        else:
            return False
        
        '''
        Solution #2
        
        d ={}
        f ={}
        for itm in s:
            if itm in d.keys():
                d[itm]+=1
            else:
                d[itm] = 1
        for itm in t:
            if itm in f.keys():
                f[itm]+=1
            else:
                f[itm] = 1
        ds = d.keys()
        fs = f.keys()
        if ds != fs:
            return False
        for k,v in d.items():
            for k1,v1 in f.items():
                if k == k1:
                    if v != v1:
                        return False
               
        return True
        
        
        
        
