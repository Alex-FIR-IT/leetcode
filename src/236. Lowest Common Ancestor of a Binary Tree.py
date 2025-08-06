
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        binary_tree = {root: None}

        stack = [root]

        while stack:
            node = stack.pop()

            if node.left:
                binary_tree[node.left] = node
                stack.append(node.left)
            if node.right:
                binary_tree[node.right] = node
                stack.append(node.right)

        p_ancestors = set()
        p_ancestor = p

        while p_ancestor is not None:
            p_ancestors.add(p_ancestor)
            p_ancestor = binary_tree.get(p_ancestor)

        q_ancestor = q

        while q_ancestor not in p_ancestors:
            q_ancestor = binary_tree.get(q_ancestor)

        return q_ancestor

