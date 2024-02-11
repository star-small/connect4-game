class Connect4:
    def __init__(self):
        self.player = "Player 2"
        self.separator = '        '
        self.board = [[self.separator for k in range(7)] for i in range(6)]
        self.finished = False
    def play(self, col):
        self.player = "Player 2" if self.player == "Player 1" else "Player 1"
        if self.finished:
            return "Game has finished!"

        row = len(self.board)-1
        while (self.board[row][col] != self.separator):
            if row==0:
                self.player = "Player 2" if self.player == "Player 1" else "Player 1"
                return "Column full!"
            row -= 1
        self.board[row][col] = self.player
        # conditions
        if(self.check_horizontal() or self.check_vertical() or self.check_diagonal_from_left() or self.check_diagonal_from_right()):
            self.finished = True
            return f"{self.player} wins!"
        #next turn
        return f"{self.player} has a turn"

    def check_horizontal(self):
        combo = 0
        for i in range(len(self.board)):
            for k in range(len(self.board[i])-1):
                if self.board[i][k] == self.board[i][k+1] and (self.board[i][k]!=self.separator):
                    combo += 1
                else:
                    combo = 0
                if combo == 3:
                    print("ewfewf")
                    return True
            combo = 0
        return False
    def check_vertical(self):
        combo = 0
        for i in range(len(self.board[0])):
            for k in range(len(self.board)-1):
                if self.board[k][i] == self.board[k + 1][i] and (self.board[k][i] != self.separator):
                    combo += 1
                else:
                    combo = 0
                if combo == 3:
                    return True
            combo = 0
        return False
    def check_diagonal_from_left(self):
        combo = 0
        # 0 a a 4 a a a
        # a 0 a a 4 a a
        # 1 a 0 2 a 4 a
        # a 1 a 0 2 a 4
        # a a 1 a 0 2 a
        # a a a 1 0 a 2
        for i in range(len(self.board)-3):
            for k in range(len(self.board[0])-3):
                if (self.board[i][k] == self.board[i+1][k+1] == self.board[i+2][k+2] == self.board[i+3][k+3]) and self.board[i][k] != self.separator:
                    return True
        return False
    def check_diagonal_from_right(self):
        combo = 0
        # a a a a a a a
        # a a a a a a a
        # a a a 1 a a a
        # a a 1 a a a 4
        # a 1 a a 0 a a
        # 1 a a a 0 a a
        for i in range(len(self.board)-3):
            for k in range(len(self.board[0])-4, len(self.board[0])):
                if (self.board[i][k] == self.board[i+1][k-1] == self.board[i+2][k-2] == self.board[i+3][k-3]) and self.board[i][k] != self.separator:
                    return True
        return False
c = Connect4()
# print(c.play(1))
# print(c.play(1))
#
# print(c.play(2))
# print(c.play(2))
#
#
# print(c.play(3))
# print(c.play(3))
#
# print(c.play(4))
# print(c.play(4))
print(c.play(4))
print(c.play(1))
print(c.play(6))
print(c.play(5))
print(c.play(4))
print(c.play(1))
print(c.play(6))
print(c.play(2))
print(c.play(2))
print(c.play(1))
print(c.play(4))
print(c.play(4))
print(c.play(3))
print(c.play(6))
print(c.play(5))
print(c.play(6))
print(c.play(0))
print(c.play(5))
print(c.play(1))
print(c.play(5))
print(c.play(0))
print(c.play(0))
"""     
        test.assert_equals(game.play(1), "Player 1 has a turn")
        test.assert_equals(game.play(1), "Player 2 has a turn")
        test.assert_equals(game.play(2), "Player 1 has a turn")
        test.assert_equals(game.play(2), "Player 2 has a turn")
        test.assert_equals(game.play(3), "Player 1 has a turn")
        test.assert_equals(game.play(3), "Player 2 has a turn")
        test.assert_equals(game.play(4), "Player 1 wins!")
        test.assert_equals(game.play(4), "Game has finished!")"""
for i in c.board:
    print(i)
