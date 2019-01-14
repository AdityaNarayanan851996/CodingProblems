# Q) 3.2: 	How would you design a stack which, in addition to push and pop, 
#			also has a function min which returns the minimum element? 
#			Push, pop and min should all operate in O(1) time.
# 			https://leetcode.com/problems/min-stack/description/
#code
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.min = []
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.min:
            
            self.min.append(x)
         
        else:
            
            t = self.min.pop()
            if x < t:
                self.min.append(t)
                self.min.append(x)
            else:
                self.min.append(t)
                self.min.append(t)
                
        self.s1.append(x)       
        #print("Pushed",x,"stack",self.s1,"Min",self.min)

    def pop(self):
        """
        :rtype: void
        """
        if self.s1:
            
            ele = self.s1.pop()
            
            ele_min = self.min.pop()
            #print('Popped',ele,'Stack',self.s1,"Min",self.min)
            
    def top(self):
        """
        :rtype: int
        """
        if self.s1:
            
            ele = self.s1.pop()
            self.s1.append(ele)
            return ele
        

    def getMin(self):
        """
        :rtype: int
        """
        #print(self.min)
        if self.min:
            ele = self.min.pop()
            self.min.append(ele)
            return ele
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()