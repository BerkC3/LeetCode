class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        result = 0
        
        while n!= 0:
            result += n % k
            n = n//k
        return result