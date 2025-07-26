# Definition for a binary tree node.
from typing import Optional
from itertools import zip_longest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    @staticmethod
    def _get_leaf_values(
            root: TreeNode
    ):
        stack = [root]

        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            elif not node.right:
                yield node.val

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        for node1, node2 in zip_longest(self._get_leaf_values(root1), self._get_leaf_values(root2)):
            if node1 != node2:
                return False

        return True
