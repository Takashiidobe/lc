from typing import Optional
from utils import TreeNode
from math import inf


# @leet start
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> float:
        """
        This problem asks for the maximum path through a tree's summed up
        node values.

        For every node, its maximum path is its current value + either its
        left or right subtree.

        If the left or right subtree have negative values, we would like to
        drop that value, so we can set it to 0 if the path is negative.

        As we traverse the tree, we want to set the current max path to
        every node's left + right + current value.
        This is because paths can go from the left subtree to the node
        to the right subtree.

        At the end we return the value that corresponds to the max path.
        """
        max_path = -inf

        def traverse(node):
            nonlocal max_path

            if not node:
                return 0

            left = max(traverse(node.left), 0)
            right = max(traverse(node.right), 0)

            max_path = max(max_path, left + right + node.val)

            return max(left + node.val, right + node.val)

        traverse(root)
        return max_path


# @leet end


def test():
    assert 2 + 2 == 4
