from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        for row_index in range(-1, -len(grid) - 1, -1):

            values = sorted(
                (
                    grid[row_index + element_index][element_index]
                    for element_index
                    in range(abs(row_index))
                ),
                reverse=True
            )

            for element_index, element in enumerate(values):
                grid[row_index + element_index][element_index] = element

        for column_index in range(1, len(grid)):
            values = sorted(
                (
                    grid[element_index][column_index + element_index]
                    for element_index
                    in range(len(grid[0]) - column_index)
                ),
                reverse=False
            )

            for index, element in enumerate(values):
                grid[index][index + column_index] = element

        return grid


if __name__ == '__main__':
    print(Solution().sortMatrix([[1, 7, 3], [9, 8, 2], [4, 5, 6]]))
