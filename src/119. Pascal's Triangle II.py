from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)

        for row_number in range(1, rowIndex + 1):
            for element_index in range(row_number - 1, 0, -1):
                row[element_index] = row[element_index] + row[element_index - 1]

        return row
