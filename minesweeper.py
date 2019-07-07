import numpy as np


class MineSweeper:
    BOMB = -1

    width = 0
    height = 0
    matrix = None

    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.matrix = [[0 for col in range(self.width)] for row in range(self.height)]

    def set_bomb_randomly(self, num_of_bomb=10):
        positions = np.random.choice(self.width * self.height, num_of_bomb, replace=False)

        for bomb in positions:
            x, y = divmod(bomb, self.width)
            self.matrix[x][y] = self.BOMB

    def calculate_map(self):
        size_of_matrix = self.width * self.height

        for i in range(size_of_matrix):
            x, y = divmod(i, self.width)

            if self.matrix[x][y] != -1:
                self.matrix[x][y] = self._num_of_bomb_near_right_here(x, y)

    def print_map(self):
        for row in self.matrix:
            print(' '.join(map(lambda x: '{:3d}'.format(x), row)))

    def _num_of_bomb_near_right_here(self, x, y) -> int:
        adjacent_elements = [((x - 1) + col, (y - 1) + row) for col in range(3) for row in range(3)]

        def _filter(item):
            if item[0] == x and item[1] == y:
                return None
            elif (0 <= item[0] < self.width) and (0 <= item[1] < self.height):
                return item
            else:
                return None

        adjacent_elements = list(filter(_filter, adjacent_elements))

        cnt = 0
        for element in adjacent_elements:
            if self.matrix[element[0]][element[1]] == -1:
                cnt += 1

        return cnt


if __name__ == '__main__':
    mine_sweeper = MineSweeper()
    mine_sweeper.set_bomb_randomly()
    mine_sweeper.calculate_map()
    mine_sweeper.print_map()
