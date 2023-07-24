class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = 1
        for i,v in enumerate(nums):
            for j in range(count,len(nums)):
                if nums[j] + v == target:
                    return i,j
            count +=1 
                
            
                    
        