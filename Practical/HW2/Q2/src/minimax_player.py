from player import Player

class MinimaxPlayer(Player):
    def __init__(self, player_number, board, depth=3):
        super().__init__(player_number, board)
        self.depth = depth

    def get_next_move(self):
        # TODO: Implement this function based on the minimax algorithm
        self.board.start_imagination()
        apply_minimax = self.recursiveMinimax(self.depth, self.player_number, self.board.get_imaginary_board().copy())
        return apply_minimax[0]

    def recursiveMinimax(self, depth, player_number, board_grid):
        best_move = None
        best_move_scores = [None, None]
        best_move_scores[player_number] = -float('inf')
        range_n = 0, self.board.get_n()
        step = 1

        if player_number == 0:
            range_n = self.board.get_n() - 1, -1
            step = -1

        for i in range(range_n[0], range_n[1], step):
            for j in range(range_n[0], range_n[1], step):
                if board_grid[i][j] == player_number:
                    for direction in self.board.get_possible_directions(player_number):
                        move = (i, j), (i + direction[0], j + direction[1])

                        if self.board.is_move_valid(board_grid, move, player_number):
                            self.board.imaginary_board_grid = board_grid.copy()
                            scores, game_over = self.board.place_piece_imaginary(move, player_number)

                            if(depth != 1 and game_over == -1):
                                scores = self.recursiveMinimax(depth - 1, 1 - player_number, self.board.imaginary_board_grid.copy())[1]
        
                            if scores[player_number] > best_move_scores[player_number]:
                                    best_move_scores = scores.copy()
                                    best_move = move

        return best_move, best_move_scores
    