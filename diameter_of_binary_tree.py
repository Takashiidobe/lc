from utils import TreeNode
from typing import Optional


# @leet start
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        To find the diameter of a binary search tree, we want to find the max
        distance between two points in the tree.
        For the final diameter that we return, we want to return the sum of
        its left and right branches.
        For counting the branches as lengths, we want to return the maximum
        of its left or right branches + 1.

        So, while we traverse the tree, we keep track of the maximum diameter,
        which is computed by each node's left + right path.

        And then for each node, we return its longer branch + 1, to count for
        the diameter of the tree.
        """
        diameter = 0

        def longest_path(node):
            nonlocal diameter
            if not node:
                return 0
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)
            diameter = max(diameter, left_path + right_path)
            return max(left_path, right_path) + 1

        longest_path(root)
        return diameter


# @leet end


def test():
    assert 2 + 2 == 4
