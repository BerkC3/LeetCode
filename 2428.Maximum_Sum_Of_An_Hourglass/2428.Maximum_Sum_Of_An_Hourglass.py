class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid[0]) 
        width = len(grid) 
        max = 0
        for i in range(0,width-2):
            for j in range(0,height-2):
                hourglass = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                if hourglass > max:
                    max =  hourglass
            
        return max