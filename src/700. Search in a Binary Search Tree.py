# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current_node = root

        while current_node and current_node.val != val:
            if current_node.val > val:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return current_node
