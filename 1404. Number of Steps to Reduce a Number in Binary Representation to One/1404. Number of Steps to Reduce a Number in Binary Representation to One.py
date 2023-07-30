class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        stepCounter = 0
        intNum = int(s,2)
        while(intNum != 1):
            if intNum % 2 == 0:
                intNum /= 2
            else:
                intNum +=1
            stepCounter +=1
            if intNum == 1 :
                break
        
        return 0 if intNum !=  1 else stepCounter    