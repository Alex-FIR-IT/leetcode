from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = float('-inf')
        rectangle_area = float('-inf')

        for dimension in dimensions:
            cur_diagonal = dimension[0] ** 2 + dimension[1] ** 2

            if cur_diagonal > max_diagonal:
                max_diagonal = cur_diagonal
                rectangle_area = dimension[0] * dimension[1]
            elif cur_diagonal == max_diagonal:
                rectangle_area = max(rectangle_area, dimension[0] * dimension[1])

        return rectangle_area


if __name__ == '__main__':
    print(Solution().areaOfMaxDiagonal([[2, 6], [5, 1], [3, 10], [8, 4]]))