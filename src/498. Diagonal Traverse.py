
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        rows_count = len(mat)
        cols_count = len(mat[0])
        result = []
        row_index = 0
        col_index = 0
        direction_up = True

        for _ in range(rows_count * cols_count):
            result.append(mat[row_index][col_index])

            if direction_up:
                if col_index == cols_count - 1:
                    row_index += 1
                    direction_up = False
                elif row_index == 0:
                    col_index += 1
                    direction_up = False
                else:
                    row_index -= 1
                    col_index += 1
            else:
                if row_index == rows_count - 1:
                    col_index += 1
                    direction_up = True
                elif col_index == 0:
                    row_index += 1
                    direction_up = True
                else:
                    row_index += 1
                    col_index -= 1

        return result