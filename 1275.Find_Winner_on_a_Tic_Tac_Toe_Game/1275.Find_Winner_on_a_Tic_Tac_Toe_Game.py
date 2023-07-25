class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        moveCounter = len(moves)

        # There are 8 possible win situations per a user: 3 for rows, 3 for columns, 1 for diagonal and 1 for backward diagonal
        # Assume that we store them all in a list called "winCon".
        # winCon[0] stands for row_1, winCon[1] stands for row_2 etc.
        winCon = [0] * 8 
        for moveNum, (row,col) in enumerate(moves):    # [[0,0],[2,0],[1,1],[2,1],[2,2]]
            if moveNum % 2 == 0:
                i = 1
            else:
                i = -1
            winCon[row] += i
            winCon[3+col] += i # [3+col] = 3 + 0 --> winCon[3]

            # winCon[2] stands for win situation by 3rd row, winCon[3] stands for win situation by 1st column

            if row == col:  # Diagonal
                winCon[6] += i
            if len(moves[0]) - row == col: #Backward diagonal
                winCon[7] +=i
            
        for totalScore in winCon:
            if totalScore == 3:
                return "A"
            elif totalScore == -3:
                return "B"
        
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
