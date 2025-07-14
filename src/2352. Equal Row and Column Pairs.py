from typing import List
from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashmap = defaultdict(int)
        pairs_count = 0

        for row in grid:
            hashmap[tuple(row)] += 1

        for column in zip(*grid):
            pairs_count += hashmap.get(tuple(column), 0)

        return pairs_count


if __name__ == '__main__':
    print(Solution().equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
