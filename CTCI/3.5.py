# Q) 3.5: 	Implement a MyQueue class which implements a queue using two stacks.
# 			https://leetcode.com/problems/implement-queue-using-stacks/description/
#code
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if self.s2:
            while self.s2:
                self.s1.append(self.s2.pop())
        
            self.s2.append(x)
            while self.s1:
                self.s2.append(self.s1.pop())
        else:
            self.s2.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.s2:
            return self.s2.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.s2:
            top = self.s2.pop()
            self.s2.append(top)
            
            return top
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        
        if not self.s2:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()