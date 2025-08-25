from typing import List
from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        reorder_count = 0
        graph = defaultdict(list)

        for connection in connections:
            graph[connection[0]].append((connection[1], 1))
            graph[connection[1]].append((connection[0], 0))

        nodes = [(0, 0)]

        while nodes:
            node, price = nodes.pop()

            if node in graph:
                nodes.extend(graph.pop(node))
                reorder_count += price

        return reorder_count

if __name__ == '__main__':
    print(Solution().minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))