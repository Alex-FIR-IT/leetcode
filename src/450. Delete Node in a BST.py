# Definition for a binary tree node.



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent_node, cur_node = None, root

        while cur_node:
            if cur_node.val == key:
                break
            if key > cur_node.val:
                parent_node, cur_node = cur_node, cur_node.right
            else:
                parent_node, cur_node = cur_node, cur_node.left
        else:
            return root  # there is no key in bst

        if cur_node.left and cur_node.right:
            node_replacement = cur_node.left
            right_child = cur_node.right

            last_right_descendant_of_left_child = node_replacement
            while last_right_descendant_of_left_child.right is not None:
                last_right_descendant_of_left_child = last_right_descendant_of_left_child.right

            last_right_descendant_of_left_child.right = right_child
        elif cur_node.right or cur_node.left:
            node_replacement = cur_node.right or cur_node.left
        else:
            node_replacement = None

        if parent_node:
            direction = 'left' if parent_node.left == cur_node else 'right'
            setattr(parent_node, direction, node_replacement)
        else:
            root = node_replacement

        return root
