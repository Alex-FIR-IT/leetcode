# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @classmethod
    def serialize(cls, node: TreeNode) -> str:
        if node is None:
            return "#"
        return f",{node.val},{cls.serialize(node.left)},{cls.serialize(node.right)}"

    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:

        root_serialized = self.serialize(root)
        subroot_serialized = self.serialize(sub_root)
        return subroot_serialized in root_serialized
