class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        temp = 30. * (minutes / 60.)
        hourDegree = hour * 30 + temp 
        minuteDegree = 360. * (minutes / 60. )
        res = abs((minuteDegree % 360.) - (hourDegree % 360.))
        
        if res > 180 : return 360 - res
        else : return res