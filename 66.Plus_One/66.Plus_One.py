class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        numAsString = ""
        for i in digits:
            numAsString += (str)(i)
        num = 1 + (int)(numAsString) 
        numAsString = (str)(num)
        temp = []
        for i in numAsString:
            temp.append((int)(i))
        return temp