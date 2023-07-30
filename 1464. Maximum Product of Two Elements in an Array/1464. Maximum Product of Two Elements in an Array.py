class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top1 = max(nums)
        nums.remove(top1)
        top2 = max(nums)
        return (top1- 1) * (top2 - 1)