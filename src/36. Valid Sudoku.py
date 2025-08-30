from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]

        for row in range(0, 9, 3):

            for column in range(0, 9, 3):
                box = []

                for box_row_index in range(3):
                    for box_column_index in range(3):
                        symbol = board[row + box_row_index][column + box_column_index]

                        if symbol.isdigit():
                            box.append(symbol)
                            rows[row + box_row_index].append(symbol)
                            columns[column + box_column_index].append(symbol)
                if len(box) != len(set(box)):
                    return False

        return all(len(row) == len(set(row)) for row in rows) and all(len(column) == len(set(column)) for column in columns)

if __name__ == '__main__':
    print(Solution().isValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))