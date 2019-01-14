# Q) 399. Evaluate Division
# 	https://leetcode.com/problems/evaluate-division/description/
#code
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        equations1 = sorted(equations)
        d = {}
        d[equations1[0][0]] = 1
        for eq in equations1:
            if eq[0] in d.keys():
                indx = equations.index(eq)
                d[eq[1]] = d[eq[0]]/values[indx] 
            elif eq[1] in d.keys():
                indx = equations.index(eq)
                d[eq[0]] = d[eq[1]] * values[indx]
        l = []
        for q in queries:
            if q in equations or list(reversed(q)) in equations:
                try:
                    indx = equations.index(q)
                    l.append(values[indx])
                except ValueError:
                    indx = equations.index(list(reversed(q)))
                    l.append(1/values[indx])
            elif q[0] in d.keys() and q[1] in d.keys():
                l.append(d[q[0]] / d[q[1]])             
            else:
                l.append(-1.0)
        return l
            
        
                
                
                
            