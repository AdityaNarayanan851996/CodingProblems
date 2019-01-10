# Q) Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer.
#  NOTE: One or two additional variables are fine. An extra copy of the array is not.
#code
class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = set()
        j = ''
        d = []
        for i in range(len(s)):
            if s[i] not in l:
                l.add(s[i])
            else:
                d.append(s[i])
        l = sorted(l)
        '''
        k = 0
        for i in range(len(l)):
            for j in range(k,len(s)):
               # print(l[i],s[j],i,j)
                if l[i] == s[j]:
                    print(l[i],s[j],i,j)
                    k = j
                    break
        
        for i in range(len(s)):
            if s[i] not in d:
                j+=s[i]
                
        print(j)
        '''
        l = ''.join((list(l)))
        
        
        return l