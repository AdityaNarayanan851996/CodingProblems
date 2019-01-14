# Q) 677. Map Sum Pairs
# 	https://leetcode.com/problems/map-sum-pairs/description/
#code
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        
    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key in self.d.keys():
            self.d.update({key:val})
        else:
            self.d[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        key_lst = self.d.keys()
        len_prefix = len(prefix)
        sums= 0
        for k in key_lst:
            if len(k) >=len_prefix:
                if prefix == k[0:len(prefix)]:
                    sums+=self.d[k]
        
        return sums
                    
                    


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)