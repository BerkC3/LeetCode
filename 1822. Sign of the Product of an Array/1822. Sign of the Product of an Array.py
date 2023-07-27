class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        for i in nums:
            if i == 0:
                return 0
            else:
                res *= i
        return -1 if res < 0 else 1