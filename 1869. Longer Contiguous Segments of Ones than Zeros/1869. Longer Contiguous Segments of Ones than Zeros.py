class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ones = s.split("0")
        zeros = s.split("1")
        
        longestOne, longestZero = -1, -1

        for i in ones:
            if len(i) > longestOne: longestOne = len(i)
        for i in zeros:
            if len(i) > longestZero: longestZero = len(i)
        
        return longestOne > longestZero

            
