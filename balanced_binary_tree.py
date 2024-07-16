from utils import TreeNode
from typing import Optional


# @leet start
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        This code checks is a binary tree is balanced.
        The balance property of a binary search tree can be said as follows:
        The depth of the left and right hand side of the tree do not vary by
        more than 1.
        Imagine a tree with a left side depth of 1 and right side of 3.
        This would not be balanced.

        To codify those rules, there's a global variable called `is_balanced`
        that verifies that the tree is balanced.
        For each node in the tree, its left and right depths are compared.
        If there is a difference of more than one, we know the tree is not balanced.
        Finally, each node returns the maximum of its left and right depth to continue
        the recursion.
        """
        is_balanced = True

        def depth(node, curr_depth):
            nonlocal is_balanced
            if not node:
                return curr_depth
            left_depth = depth(node.left, curr_depth + 1)
            right_depth = depth(node.right, curr_depth + 1)
            if abs(right_depth - left_depth) > 1:
                is_balanced = False
            return max(left_depth, right_depth)

        depth(root, 0)
        return is_balanced


# @leet end


def test():
    assert 2 + 2 == 4
