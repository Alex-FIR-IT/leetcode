# Definition for a binary tree node.
from typing import Optional, List

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = deque()
        stack.append((root, 1))

        visible_nodes = []
        current_level = 0

        while stack:
            node, level = stack.popleft()

            if current_level < level:
                visible_nodes.append(node.val)
                current_level = level

            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))

        return visible_nodes
