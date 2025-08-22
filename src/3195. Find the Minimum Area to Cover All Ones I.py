from typing import List


class Solution:

    def _find(self, lst: List[int], value: int) -> int | None:
        try:
            idx = lst.index(value)
        except ValueError:
            idx = None

        return idx

    def _rfind(self, lst: List[int], value: int, default_value: int) -> int:
        for idx, lst_value in enumerate(reversed(lst), start=1):
            if lst_value == value:
                return len(lst) - idx

        return default_value

    def minimumArea(self, grid: List[List[int]]) -> int:
        width_start = float('inf')
        width_end = float('-inf')
        height_start = None
        height_end = None

        for row_idx, row in enumerate(grid):
            one_idx = self._find(row, 1)

            if one_idx is not None:
                width_start = min(width_start, one_idx)

                width_end = max(width_end, self._rfind(row, 1, width_end))

            if one_idx is not None:
                height_end = row_idx

                if height_start is None:
                    height_start = row_idx

        return (width_end - width_start + 1) * (height_end - height_start + 1)


if __name__ == '__main__':
    print(Solution().minimumArea([[1, 0], [0, 0]]))