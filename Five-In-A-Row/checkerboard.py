from collections import namedtuple

Chess = namedtuple('Chess', 'Name Value Color')
Position = namedtuple('Position', 'X Y')

Black = Chess('black', 1, (45, 45, 45))
White = Chess('white', 2, (219, 219, 219))

vector = [(1, 0), (0, 1), (1, 1), (1, -1)]


class Check_all:
    def __init__(self, node_numbers):
        self._node_numbers = node_numbers
        self._board = [[0] * node_numbers for _ in range(node_numbers)]

    def _get_board(self):
        return self._board

    checkerboard = property(_get_board)

    # be able to drop or not
    def able_to_drop(self, position):
        return self._board[position.Y][position.X] == 0

    def step(self, chess, position):
        
        print(f'{chess.Name} ({position.X}, {position.Y})')
        self._board[position.Y][position.X] = chess.Value

        if self._win(position):
            print(f'{chess.Name} win')
            return chess

    # determine win or not
    def _win(self, position):
        current_value = self._board[position.Y][position.X]
        for v in vector:
            if self._get_count_of_nodes(position, current_value, v[0], v[1]):
                return True

    def _get_count_of_nodes(self, position, value, x_vector, y_vector):
        count = 1
        for step in range(1, 5):
            x = position.X + step * x_vector
            y = position.Y + step * y_vector
            if 0 <= x < self._node_numbers and 0 <= y < self._node_numbers and self._board[y][x] == value:
                count += 1
            else:
                break
        for step in range(1, 5):
            x = position.X - step * x_vector
            y = position.Y - step * y_vector
            if 0 <= x < self._node_numbers and 0 <= y < self._node_numbers and self._board[y][x] == value:
                count += 1
            else:
                break

        return count >= 5
