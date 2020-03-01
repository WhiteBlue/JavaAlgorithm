from typing import List

SQUARE_MARK = "O"
TMP_MARK = "Z"
NON_MARK = "X"


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        x_size = len(board)
        y_size = 0
        if board:
            y_size = len(board[0])
        for i in range(x_size):
            if board[i][0] == SQUARE_MARK:
                self.find_recursive(i, 0, x_size, y_size, board)

            if board[i][y_size - 1] == SQUARE_MARK:
                self.find_recursive(i, y_size - 1, x_size, y_size, board)

        for i in range(y_size):
            if board[0][i] == SQUARE_MARK:
                self.find_recursive(0, i, x_size, y_size, board)
            if board[x_size - 1][i] == SQUARE_MARK:
                self.find_recursive(x_size - 1, i, x_size, y_size, board)

        for i in range(x_size):
            for j in range(y_size):
                if board[i][j] == SQUARE_MARK:
                    board[i][j] = NON_MARK
                elif board[i][j] == TMP_MARK:
                    board[i][j] = SQUARE_MARK

    def find_recursive(self, x: int, y: int, x_size: int, y_size: int, board: List[List[str]]):
        board[x][y] = TMP_MARK
        if x != 0 and board[x - 1][y] == SQUARE_MARK:
            self.find_recursive(x - 1, y, x_size, y_size, board)
        if x != x_size - 1 and board[x + 1][y] == SQUARE_MARK:
            self.find_recursive(x + 1, y, x_size, y_size, board)
        if y != 0 and board[x][y - 1] == SQUARE_MARK:
            self.find_recursive(x, y - 1, x_size, y_size, board)
        if y != y_size - 1 and board[x][y + 1] == SQUARE_MARK:
            self.find_recursive(x, y + 1, x_size, y_size, board)


if __name__ == '__main__':
    s = Solution()

    board = [["X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X"], ["X", "O", "X", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "X"]]

    for l in board:
        print(l)

    print("===========")

    s.solve(board)

    for l in board:
        print(l)
