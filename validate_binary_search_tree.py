from typing import Optional
from utils import TreeNode
from math import inf


# @leet start
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        This function determines whether a given binary search tree is valid.
        The property of a binary search tree is as follows:
        The node's value is greater than the value of its left child, but
        less than the value of its right child.

        This goes all the way down the tree.
        Thus, for the first node, we allow any value for the root.
        For the left subtree, the value can be within [-inf..node.val]
        For the right subtree, the value can be within [node.val..inf]
        So, the condition for checking for the validity of the left subtree is
        that it must fall between [previously_allowed_min..node.val]
        And for the right subtree, [node.val..previosuly_allowed_max]
        We pass this condition through the tree to get the desired result.
        """

        def traverse(node, min_allowed, max_allowed):
            if not node:
                return True
            node_valid = min_allowed < node.val < max_allowed
            left_valid = traverse(node.left, min_allowed, node.val)
            right_valid = traverse(node.right, node.val, max_allowed)
            return all([node_valid, left_valid, right_valid])

        return traverse(root, -inf, inf)


# @leet end


def test():
    assert 2 + 2 == 4
