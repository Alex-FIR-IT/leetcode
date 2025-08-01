# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(
                node: Optional[TreeNode],
                direction: int = None,
                current_zigzag: int = 0
        ) -> int:

            if node is None:
                return current_zigzag

            left_zigzag = current_zigzag + 1 if direction == 0 else 0
            left_zigzag = dfs(node.left, direction=1, current_zigzag=left_zigzag)

            right_zigzag = current_zigzag + 1 if direction == 1 else 0
            right_zigzag = dfs(node.right, direction=0, current_zigzag=right_zigzag)

            return max(left_zigzag, right_zigzag)
        return dfs(root)
