class SmartAgent:
    def __init__(self, board):
        self.board = board

    def gameMove(self):
        board_matrix = self.board

        def verifyBestPlay(board_matrix):
            near_spaces = [(1,0), (-1, 0), (0,1), (0, -1)]
            far_spaces = [(2,0), (-2, 0), (0,2), (0, -2)]

            if board_matrix[1][1] != 1 and board_matrix[1][1] != 2:
                return [1, 1]

            # print(board_matrix)

            for i in range(len(board_matrix)):
                for j in range(len(board_matrix[i])):
                    current_position = board_matrix[i][j]
                    if current_position == 1:
                        for x, y in near_spaces:
                            col, row = (current_position + x), (current_position + y)
                            if board_matrix[x][y] == 1:
                                if board_matrix[row][col] == 2:
                                    pass
                                else: 
                                    return [row, col]
                            elif board_matrix[x][y] == 2:
                                pass
                        for x, y in far_spaces:
                            if board_matrix[x][y] == 1:
                                if board_matrix[row][col] == 2:
                                    pass
                                else: 
                                    return [row, col]
                            elif board_matrix[x][y] == 2:
                                pass

        return verifyBestPlay(board_matrix)

if __name__=="__main__":    
    agente = SmartAgent([[1, 0, 0], 
                         [2, 2, 1], 
                         [1, 0, 0]])
    print(agente.gameMove())
