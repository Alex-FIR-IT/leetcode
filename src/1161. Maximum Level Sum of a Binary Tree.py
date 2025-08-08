# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])
        best_level = 1
        best_level_sum = float('-inf')
        current_level_index = 1

        while queue:
            level_node_count = len(queue)
            level_sum = 0

            for _ in range(level_node_count):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > best_level_sum:
                best_level_sum = level_sum
                best_level = current_level_index

            current_level_index += 1

        return best_level
